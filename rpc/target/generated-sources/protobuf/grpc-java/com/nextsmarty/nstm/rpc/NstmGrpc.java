package com.nextsmarty.nstm.rpc;

import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.4.0)",
    comments = "Source: services.proto")
public final class NstmGrpc {

  private NstmGrpc() {}

  public static final String SERVICE_NAME = "com.nextsmarty.nstm.rpc.Nstm";

  // Static method descriptors that strictly reflect the proto.
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<com.nextsmarty.nstm.rpc.Services.PullTaskRequest,
      com.nextsmarty.nstm.rpc.Services.PullTaskRespone> METHOD_PULL_TASK =
      io.grpc.MethodDescriptor.<com.nextsmarty.nstm.rpc.Services.PullTaskRequest, com.nextsmarty.nstm.rpc.Services.PullTaskRespone>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "com.nextsmarty.nstm.rpc.Nstm", "PullTask"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.PullTaskRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.PullTaskRespone.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<com.nextsmarty.nstm.rpc.Services.DoneTaskRequest,
      com.nextsmarty.nstm.rpc.Services.DoneTaskRespone> METHOD_DONE_TASK =
      io.grpc.MethodDescriptor.<com.nextsmarty.nstm.rpc.Services.DoneTaskRequest, com.nextsmarty.nstm.rpc.Services.DoneTaskRespone>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "com.nextsmarty.nstm.rpc.Nstm", "DoneTask"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.DoneTaskRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.DoneTaskRespone.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest,
      com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone> METHOD_REGISTER =
      io.grpc.MethodDescriptor.<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest, com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "com.nextsmarty.nstm.rpc.Nstm", "Register"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest,
      com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone> METHOD_SUBMIT_TASK =
      io.grpc.MethodDescriptor.<com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest, com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "com.nextsmarty.nstm.rpc.Nstm", "SubmitTask"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone.getDefaultInstance()))
          .build();
  @io.grpc.ExperimentalApi("https://github.com/grpc/grpc-java/issues/1901")
  public static final io.grpc.MethodDescriptor<com.nextsmarty.nstm.rpc.Services.DeleteRequest,
      com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone> METHOD_DELETE_TASK =
      io.grpc.MethodDescriptor.<com.nextsmarty.nstm.rpc.Services.DeleteRequest, com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone>newBuilder()
          .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
          .setFullMethodName(generateFullMethodName(
              "com.nextsmarty.nstm.rpc.Nstm", "DeleteTask"))
          .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.DeleteRequest.getDefaultInstance()))
          .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
              com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone.getDefaultInstance()))
          .build();

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static NstmStub newStub(io.grpc.Channel channel) {
    return new NstmStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static NstmBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new NstmBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static NstmFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new NstmFutureStub(channel);
  }

  /**
   */
  public static abstract class NstmImplBase implements io.grpc.BindableService {

    /**
     */
    public void pullTask(com.nextsmarty.nstm.rpc.Services.PullTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.PullTaskRespone> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_PULL_TASK, responseObserver);
    }

    /**
     */
    public void doneTask(com.nextsmarty.nstm.rpc.Services.DoneTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DoneTaskRespone> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_DONE_TASK, responseObserver);
    }

    /**
     */
    public void register(com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_REGISTER, responseObserver);
    }

    /**
     */
    public void submitTask(com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_SUBMIT_TASK, responseObserver);
    }

    /**
     */
    public void deleteTask(com.nextsmarty.nstm.rpc.Services.DeleteRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone> responseObserver) {
      asyncUnimplementedUnaryCall(METHOD_DELETE_TASK, responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            METHOD_PULL_TASK,
            asyncUnaryCall(
              new MethodHandlers<
                com.nextsmarty.nstm.rpc.Services.PullTaskRequest,
                com.nextsmarty.nstm.rpc.Services.PullTaskRespone>(
                  this, METHODID_PULL_TASK)))
          .addMethod(
            METHOD_DONE_TASK,
            asyncUnaryCall(
              new MethodHandlers<
                com.nextsmarty.nstm.rpc.Services.DoneTaskRequest,
                com.nextsmarty.nstm.rpc.Services.DoneTaskRespone>(
                  this, METHODID_DONE_TASK)))
          .addMethod(
            METHOD_REGISTER,
            asyncUnaryCall(
              new MethodHandlers<
                com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest,
                com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone>(
                  this, METHODID_REGISTER)))
          .addMethod(
            METHOD_SUBMIT_TASK,
            asyncUnaryCall(
              new MethodHandlers<
                com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest,
                com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone>(
                  this, METHODID_SUBMIT_TASK)))
          .addMethod(
            METHOD_DELETE_TASK,
            asyncUnaryCall(
              new MethodHandlers<
                com.nextsmarty.nstm.rpc.Services.DeleteRequest,
                com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone>(
                  this, METHODID_DELETE_TASK)))
          .build();
    }
  }

  /**
   */
  public static final class NstmStub extends io.grpc.stub.AbstractStub<NstmStub> {
    private NstmStub(io.grpc.Channel channel) {
      super(channel);
    }

    private NstmStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NstmStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new NstmStub(channel, callOptions);
    }

    /**
     */
    public void pullTask(com.nextsmarty.nstm.rpc.Services.PullTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.PullTaskRespone> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_PULL_TASK, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void doneTask(com.nextsmarty.nstm.rpc.Services.DoneTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DoneTaskRespone> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_DONE_TASK, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void register(com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_REGISTER, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void submitTask(com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_SUBMIT_TASK, getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void deleteTask(com.nextsmarty.nstm.rpc.Services.DeleteRequest request,
        io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(METHOD_DELETE_TASK, getCallOptions()), request, responseObserver);
    }
  }

  /**
   */
  public static final class NstmBlockingStub extends io.grpc.stub.AbstractStub<NstmBlockingStub> {
    private NstmBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private NstmBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NstmBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new NstmBlockingStub(channel, callOptions);
    }

    /**
     */
    public com.nextsmarty.nstm.rpc.Services.PullTaskRespone pullTask(com.nextsmarty.nstm.rpc.Services.PullTaskRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_PULL_TASK, getCallOptions(), request);
    }

    /**
     */
    public com.nextsmarty.nstm.rpc.Services.DoneTaskRespone doneTask(com.nextsmarty.nstm.rpc.Services.DoneTaskRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_DONE_TASK, getCallOptions(), request);
    }

    /**
     */
    public com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone register(com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_REGISTER, getCallOptions(), request);
    }

    /**
     */
    public com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone submitTask(com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_SUBMIT_TASK, getCallOptions(), request);
    }

    /**
     */
    public com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone deleteTask(com.nextsmarty.nstm.rpc.Services.DeleteRequest request) {
      return blockingUnaryCall(
          getChannel(), METHOD_DELETE_TASK, getCallOptions(), request);
    }
  }

  /**
   */
  public static final class NstmFutureStub extends io.grpc.stub.AbstractStub<NstmFutureStub> {
    private NstmFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private NstmFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected NstmFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new NstmFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.nextsmarty.nstm.rpc.Services.PullTaskRespone> pullTask(
        com.nextsmarty.nstm.rpc.Services.PullTaskRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_PULL_TASK, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.nextsmarty.nstm.rpc.Services.DoneTaskRespone> doneTask(
        com.nextsmarty.nstm.rpc.Services.DoneTaskRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_DONE_TASK, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone> register(
        com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_REGISTER, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone> submitTask(
        com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_SUBMIT_TASK, getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone> deleteTask(
        com.nextsmarty.nstm.rpc.Services.DeleteRequest request) {
      return futureUnaryCall(
          getChannel().newCall(METHOD_DELETE_TASK, getCallOptions()), request);
    }
  }

  private static final int METHODID_PULL_TASK = 0;
  private static final int METHODID_DONE_TASK = 1;
  private static final int METHODID_REGISTER = 2;
  private static final int METHODID_SUBMIT_TASK = 3;
  private static final int METHODID_DELETE_TASK = 4;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final NstmImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(NstmImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_PULL_TASK:
          serviceImpl.pullTask((com.nextsmarty.nstm.rpc.Services.PullTaskRequest) request,
              (io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.PullTaskRespone>) responseObserver);
          break;
        case METHODID_DONE_TASK:
          serviceImpl.doneTask((com.nextsmarty.nstm.rpc.Services.DoneTaskRequest) request,
              (io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DoneTaskRespone>) responseObserver);
          break;
        case METHODID_REGISTER:
          serviceImpl.register((com.nextsmarty.nstm.rpc.Services.WorkerRegisterRequest) request,
              (io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.WorkerRegisterRespone>) responseObserver);
          break;
        case METHODID_SUBMIT_TASK:
          serviceImpl.submitTask((com.nextsmarty.nstm.rpc.Services.SubmitTaskRequest) request,
              (io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.SubmitTaskRespone>) responseObserver);
          break;
        case METHODID_DELETE_TASK:
          serviceImpl.deleteTask((com.nextsmarty.nstm.rpc.Services.DeleteRequest) request,
              (io.grpc.stub.StreamObserver<com.nextsmarty.nstm.rpc.Services.DeleteTaskRespone>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static final class NstmDescriptorSupplier implements io.grpc.protobuf.ProtoFileDescriptorSupplier {
    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return com.nextsmarty.nstm.rpc.Services.getDescriptor();
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (NstmGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new NstmDescriptorSupplier())
              .addMethod(METHOD_PULL_TASK)
              .addMethod(METHOD_DONE_TASK)
              .addMethod(METHOD_REGISTER)
              .addMethod(METHOD_SUBMIT_TASK)
              .addMethod(METHOD_DELETE_TASK)
              .build();
        }
      }
    }
    return result;
  }
}
