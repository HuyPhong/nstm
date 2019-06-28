package com.nextsmarty.nstm.client;

import com.google.gson.Gson;
import com.nextsmarty.nstm.rpc.NstmGrpc;
import com.nextsmarty.nstm.rpc.Services;
import io.grpc.*;
import org.apache.commons.cli.*;

import javax.swing.text.TabableView;
import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.NotActiveException;

public class Client {

    private Channel channel;
    private NstmGrpc.NstmBlockingStub stub;

    public Client(Channel channel){
        this.channel = channel;
        this.stub = NstmGrpc.newBlockingStub(channel);
    }

    public static void main(String[] args){

        Channel channel = ManagedChannelBuilder.forAddress("127.0.0.1", 8000).usePlaintext().build();
        Client client = new Client(channel);

        Options options = new Options();
        options.addOption("s", false, "Submit task");
        options.addOption("n", true, "Task name");
        options.addOption("r", true, "remmote uri");
        options.addOption("d", true, "Delete task");
        CommandLineParser parser = new DefaultParser();
        try {
            CommandLine cmd = parser.parse(options, args);
            if(cmd.hasOption("s")){
                Services.TaskDescr.Builder builder = Services.TaskDescr.newBuilder();
                if(cmd.hasOption("n") &&  cmd.hasOption("r")){
                    builder.setTaskName(cmd.getOptionValue("n"))
                            .setRemoteUri(cmd.getOptionValue("r"));
                    Services.SubmitTaskRespone ack = client.submitTask(builder.build());
                    System.out.println(ack.getAck());
                }
                else {
                    System.out.println("Submit task: -s -n <task_name> -g <git_url> -b <git_branch>");
                }
            }
            else if(cmd.hasOption("d")){
                System.out.println(client.deleteTask(cmd.getOptionValue("d")));
            }
        } catch (ParseException e) {
            e.printStackTrace();
        }


    }

    public Services.SubmitTaskRespone submitTask(Services.TaskDescr descr){
        try{
            return stub.submitTask(Services.SubmitTaskRequest.newBuilder().setTaskDescr(descr).build());
        }
        catch (Exception e)
        {
            System.out.println(((StatusRuntimeException)e).getStatus());
            e.printStackTrace();
            return null;
        }
    }
    public Services.DeleteTaskRespone deleteTask(String taskName){
        return stub.deleteTask(Services.DeleteRequest.newBuilder().setTaskName(taskName).build());
    }

}
