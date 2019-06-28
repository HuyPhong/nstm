package com.nextsmarty.nstm.server;

import com.nextsmarty.nstm.rpc.Services;
import javafx.concurrent.Task;
import org.apache.curator.framework.CuratorFramework;
import org.apache.curator.framework.CuratorFrameworkFactory;
import org.apache.curator.framework.api.transaction.CuratorOp;
import org.apache.curator.framework.recipes.cache.PathChildrenCache;
import org.apache.curator.retry.ExponentialBackoffRetry;

import org.apache.zookeeper.CreateMode;
import org.apache.zookeeper.KeeperException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.TimeUnit;

public class Manager implements Runnable{

    private static Logger logger = LoggerFactory.getLogger(Manager.class);

    public static final Manager instance = new Manager();
    public static final String TASK_PATH = "/tasks";
    public static final String QUEUE_PATH = "/queue";
    public static final String WORKER_PATH = "/workers";
    public static final String MASTER_PATH = "/master";

    private CuratorFramework client;

    private PathChildrenCache queueCache;
    private PathChildrenCache workerCache;
    private Services.MasterDesc masterDesc;
    private ConcurrentHashMap<String, Worker> workers;
    private ConcurrentHashMap<String, String> assigned;


    public CuratorFramework getZooClient(){
        return this.client;
    }

    public static boolean init() throws Exception{
        instance.masterDesc = Services.MasterDesc.newBuilder()
                .setIp("127.0.0.1")
                .setGrpcPort(8000)
                .build();
        if(!instance.initZooClient())
        {
            return false;
        }

        try {
            instance.client.create().withMode(CreateMode.PERSISTENT).forPath(TASK_PATH);
        }
        catch (KeeperException.NodeExistsException e){
            logger.info(e.getMessage());
        }
        try{
            instance.client.create().withMode(CreateMode.PERSISTENT).forPath(QUEUE_PATH);
        }
        catch (KeeperException.NodeExistsException e)
        {
            logger.info(e.getMessage());
        }

        try{
            instance.client.create().withMode(CreateMode.PERSISTENT).forPath(MASTER_PATH, instance.masterDesc.toByteArray());
        }
        catch (KeeperException.NodeExistsException e){

        }

        instance.workers = new ConcurrentHashMap<>();
        instance.workerCache = new PathChildrenCache(instance.client, "/workers", true);
        instance.workerCache.getListenable().addListener((client, event) -> {
            try{
                switch (event.getType()){
                    case CHILD_ADDED:
                        Services.WorkerDesc desc = Services.WorkerDesc.parseFrom(event.getData().getData());
                        instance.workers.put(event.getData().getPath().replace(WORKER_PATH + "/", ""),
                                new Worker(desc));
                        break;
                    case CHILD_REMOVED:
                        String workerId = event.getData().getPath().replace(WORKER_PATH + "/", "");
                        instance.workerRemoveHandler(workerId);
                        break;
                }
            }
            catch (Exception e){
                e.printStackTrace();
            }
        });

        instance.queueCache = new PathChildrenCache(instance.client, "/queue", true);
        instance.queueCache.getListenable().addListener((client, event) -> {
            try{
                switch (event.getType()){
                    case CHILD_ADDED:
                        Tasks.add(Services.TaskDescr.parseFrom(event.getData().getData()));
                        break;
                    case CHILD_REMOVED:
                        //String task_name = event.getData().getPath().replace("/queue/", "");
                        //Tasks.remove(task_name);
                }
            }
            catch (Exception e){

            }
        });
        instance.queueCache.start();
        instance.workerCache.start();
        return true;
    }

    public void workerRemoveHandler(String workerId){
        this.workers.get(workerId).recoverTask();
        workers.remove(workerId);
    }

    public boolean initZooClient(){
        System.out.println(Config.instance.zookeeper_uri);
        client = CuratorFrameworkFactory.newClient(Config.instance.zookeeper_uri,
                new ExponentialBackoffRetry(100, 20));
        client.start();
        try {
            client.blockUntilConnected(3, TimeUnit.SECONDS);
            if(client.getZookeeperClient().isConnected())
            {
                logger.info("CuratorFramework connect success to zookeeper server");
                return true;
            }
        } catch (InterruptedException e) {
            logger.error(e.getMessage());
        }
        logger.info("CuratorFrameWork connect fail to zookeeper server");
        return false;

    }

    public Services.SubmitTaskRespone submitTask(Services.SubmitTaskRequest request) throws Exception {
        Services.SubmitTaskRespone.Builder builder = Services.SubmitTaskRespone.newBuilder();
        try {
            Services.TaskDescr taskDescr = request.getTaskDescr();
            List<CuratorOp> list = new ArrayList<>();
            list.add(client.transactionOp().create().forPath(TASK_PATH + "/" + taskDescr.getTaskName(), taskDescr.toByteArray()));
            list.add(client.transactionOp().create().forPath(QUEUE_PATH + "/" + taskDescr.getTaskName(), taskDescr.toByteArray()));
            client.transaction().forOperations(list);
            builder.setAck(Services.Ack.SUBMIT_SUCCESS);
        } catch (KeeperException.NodeExistsException e) {
            logger.error(e.getMessage());
            builder.setAck(Services.Ack.SUBMIT_FAILURE_EXISTS);
        }
        catch (Exception e)
        {
            logger.error(e.getMessage());
            throw e;
        }
        return builder.build();
    }
    public Services.DeleteTaskRespone deleteTask(Services.DeleteRequest request) throws Exception {
        Services.DeleteTaskRespone.Builder builder = Services.DeleteTaskRespone.newBuilder();
        try{
            List<CuratorOp> list = new ArrayList<>();
            list.add(client.transactionOp().delete().forPath(TASK_PATH + "/" + request.getTaskName()));
            list.add(client.transactionOp().delete().forPath(QUEUE_PATH + "/" + request.getTaskName()));
            client.transaction().forOperations(list);
            Tasks.remove(request.getTaskName());
            builder.setAck(Services.Ack.DELETE_SUCCESS);
        } catch (KeeperException.NoNodeException e) {
            builder.setAck(Services.Ack.DELETE_FAILURE_TASK_NOT_EXISTS);
        }
        catch (Exception e)
        {
            throw e;
        }
        return builder.build();
    }

    public Services.PullTaskRespone pullTask(Services.PullTaskRequest request) {
        Tasks.Task task = Tasks.getFirstSastify();
        Worker worker = workers.get(request.getWorkerId());
        Services.PullTaskRespone.Builder builder = Services.PullTaskRespone.newBuilder();
        if(task != null){
            builder.setTaskDescr(task.getDescr());
            builder.setAck(Services.Ack.PULL_TASK_SUCCESS);
            task.assign(request.getWorkerId());
            worker.assginTask(task.getDescr().getTaskName());
        }
        else{
            builder.setAck(Services.Ack.PULL_TASK_NO_TASK_SASTIFY);
        }
        return builder.build();
    }

    public Services.DoneTaskRespone doneTask(Services.DoneTaskRequest request){
        Services.DoneTaskRespone.Builder builder = Services.DoneTaskRespone.newBuilder();
        Tasks.remove(request.getTaskName());

        try {
            List<CuratorOp> list = new ArrayList<>();
            String data;
            if(request.getIsSuccess()){
                data = Tasks.Task.SUCCESS_STATUS;
            }
            else {
                data = Tasks.Task.FAIL_STATUS;
            }
            try{
                client.create().withMode(CreateMode.PERSISTENT).forPath(TASK_PATH + "/" + request.getTaskName() +
                        "/status", data.getBytes());
            }
            catch (KeeperException.NodeExistsException e)
            {
                logger.warn(e.getMessage());
                list.add(client.transactionOp().setData().forPath(TASK_PATH + "/" + request.getTaskName() + "/status",
                        data.getBytes()));
            }
            list.add(client.transactionOp().delete().forPath(QUEUE_PATH + "/" + request.getTaskName()));
            client.transaction().forOperations(list);
            builder.setAck(Services.Ack.DONE_TASK_SUCCESS);
        } catch (Exception e) {
            logger.error(e.getMessage());
            builder.setAck(Services.Ack.DONE_TASK_FAILURE);
        }
        return builder.build();
    }

    public Worker getWorker(String workerId){
        return workers.get(workerId);
    }
    @Override
    public void run() {
        while (true){
            try {
                Thread.sleep(1000);
                System.out.println(Tasks.unassignedTasksSize());
                //System.out.println(Task.size());
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}
