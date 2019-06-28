package com.nextsmarty.nstm.server;

import org.apache.log4j.BasicConfigurator;
import org.apache.log4j.ConsoleAppender;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import com.nextsmarty.nstm.server.logging.*;

public class Main {
    static Logger logger = LoggerFactory.getLogger(Main.class);
    public static void main(String[] args) throws IOException, InterruptedException{
        BasicConfigurator.configure();
        try {
            if(!Manager.init()){
                logger.info("Init failure, turn off");
                System.exit(1);
            }
        } catch (Exception e) {
            e.printStackTrace();
            System.exit(1);
        }

        GrpcServer.instance.initAndStartServer();
        new Thread(Manager.instance).start();
        RestServer.instance.start();
}

/*
    private static class Worker2ManagerIml extends com.nextsmarty.nstm.rpc.Worker2ManagerGrpc.Worker2ManagerImplBase{

        @Override
        public void pullTask(WorkerMetrics request, StreamObserver<Services.Task> responseObserver) {
            System.out.println(request.getGpu());
            responseObserver.onNext(Task.newBuilder().setCmd("ls").setName("kkkk").build());
            responseObserver.onCompleted();
        }
    }

 */
}
