package com.nextsmarty.nstm.client;

import java.util.concurrent.ConcurrentHashMap;

public class Main {
    public static void main(String[] args){
        ConcurrentHashMap<Integer, Integer> map = new ConcurrentHashMap<>();
        System.out.println(map.get(1));
    }
}
