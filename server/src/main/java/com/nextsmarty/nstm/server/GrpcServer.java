package com.nextsmarty.nstm.server;

import com.nextsmarty.nstm.rpc.NstmGrpc;
import com.nextsmarty.nstm.rpc.Services;
import io.grpc.*;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;


public class GrpcServer {

    public static final GrpcServer instance = new GrpcServer();

    private static Logger logger = LoggerFactory.getLogger(GrpcServer.class);

    private int port;
    private Server server;


    public static class NstmService extends NstmGrpc.NstmImplBase {
        @Override
        public void submitTask(com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest request,
                               io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone> responseObserver) {
            try {
                responseObserver.onNext(Manager.instance.submitTask(request));
            } catch (Exception e) {
                StatusException exception = Status.ALREADY_EXISTS.withDescription(e.getMessage()).asException();
                responseObserver.onError(exception);
            }
            //responseObserver.onNext(Services.SubmitTaskAck.newBuilder().setAck(Services.SubmitAck.SUCCESS).build());
            responseObserver.onCompleted();
        }
        @Override
        public void deleteTask(com.nextsmarty.nstm.rpc.Services.DeleteRequest request,
                               io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone> responseObserver)
        {
            try {
                responseObserver.onNext(Manager.instance.deleteTask(request));
            } catch (Exception e) {
                responseObserver.onError(e);
            }
            responseObserver.onCompleted();
        }
        @Override
        public void pullTask(com.nextsmarty.nstm.rpc.Services.PullTaskRequest request,
                             io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.PullTaskRespone> responseObserver) {
                responseObserver.onNext(Manager.instance.pullTask(request));
                responseObserver.onCompleted();

        }

        @Override
        public void doneTask(com.nextsmarty.nstm.rpc.Services.DoneTaskRequest request,
                             io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DoneTaskRespone> responseObserver) {
            responseObserver.onNext(Manager.instance.doneTask(request));
            responseObserver.onCompleted();
        }
        @Override
        public void register(com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest request,
                             io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone> responseObserver) {
            Services.WorkerRegisterRespone.Builder builder = Services.WorkerRegisterRespone.newBuilder();
            System.out.println(request.getWorkerId());
            if(Manager.instance.getWorker(request.getWorkerId()) != null){
                builder.setAck(Services.Ack.REGISTER_SUCCESS);
            }
            else{
                builder.setAck(Services.Ack.REGISTER_FAIL);
            }
            responseObserver.onNext(builder.build());
            responseObserver.onCompleted();
        }

    }
    public boolean initAndStartServer(){
        this.port = Config.instance.grpc_port;
        this.server = ServerBuilder.forPort(port)
                .addService(new NstmService())
                .build();
        try {
            this.server.start();
            logger.info("Grpc server started");
            return true;
        } catch (IOException e) {
            logger.error("Error when start Grpc server: " + e.getMessage());
        }
        return false;
    }
}
