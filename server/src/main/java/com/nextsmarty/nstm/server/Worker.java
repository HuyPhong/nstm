package com.nextsmarty.nstm.server;

import com.nextsmarty.nstm.rpc.Services;

import java.util.HashSet;
import java.util.Iterator;
import java.util.Objects;
import java.util.Set;

public class Worker {

    private Services.WorkerDesc desc;
    private Set<String> assignedTasks;

    public Worker(Services.WorkerDesc desc) {
        this.desc = desc;
        this.assignedTasks = new HashSet<>();
    }

    public void assginTask(String taskName){
        assignedTasks.add(taskName);
    }

    public void recoverTask(){
        assignedTasks.forEach(taskName ->{
            Tasks.Task task = Tasks.get(taskName);
            if(task != null){
                task.recover();
            }
        });
    }
}
