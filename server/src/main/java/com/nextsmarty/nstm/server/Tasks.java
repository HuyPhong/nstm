package com.nextsmarty.nstm.server;

import com.nextsmarty.nstm.rpc.Services;

import java.util.concurrent.ConcurrentHashMap;
import java.util.concurrent.atomic.AtomicInteger;

public class Tasks {

    private static final ConcurrentHashMap<String, Task> tasks = new ConcurrentHashMap<>();
    private static Task head;
    private static Task tail;

    public static class Task

    {
        public static final String SUCCESS_STATUS = "success";
        public static final String FAIL_STATUS = "fail";

        private Services.TaskDescr descr;
        private Task prev;
        private Task next;
        private String assigned;


        public void assign (String workerId){
            this.assigned = workerId;
        }

        public void recover () {
            this.assigned = null;
        }

        public Services.TaskDescr getDescr () {
            return this.descr;
        }

        public boolean isAssigned(){
            return this.assigned != null;
        }
    }
    public static Task add (Services.TaskDescr taskDescr){
        Task task = new Task();
        task.descr = taskDescr;
        task.assigned = null;
        if (Tasks.head == null) {
            Tasks.head = Tasks.tail = task;
            task.next = null;
            task.prev = null;
        } else {
            task.prev = tail;
            task.next = null;
            tail.next = task;
            tail = task;
        }
        tasks.put(taskDescr.getTaskName(), task);
        return task;
    }
    public static Task remove (String taskName){
        if (!tasks.containsKey(taskName))
            return null;
        Task task = tasks.get(taskName);
        tasks.remove(taskName);
        if (tasks.size() == 1) {
            head = tail = null;
            return task;
        }
        Task prev = task.prev;
        Task next = task.next;
        task.next = null;
        task.prev = null;
        if (Tasks.isHead(task)) {
            head = next;
            return task;
        }
        if (Tasks.isTail(task)) {
            task = prev;
            return task;
        }
        prev.next = next;
        next.prev = prev;
        return task;
    }
    public static Task get (String taskName){
        return tasks.get(taskName);
    }

    public static int size () {
        return tasks.size();
    }

    public static boolean isHead (Task task){
        return task == head;
    }

    public static boolean isTail (Task task){
        return task == tail;
    }

    public static Task getFirstSastify () {
        Task tmp = head;
        while (tmp != null) {
            if (tmp.assigned == null) {
                break;
            }
            tmp = tmp.next;
        }
        return tmp;
    }

    public static int unassignedTasksSize(){
        AtomicInteger size = new AtomicInteger(0);
        tasks.values().forEach(task -> {
            if(!task.isAssigned())
                size.getAndIncrement();
        });
        return size.get();
    }

}
