package com.nextsmarty.nstm.server;

import com.google.gson.Gson;

import java.io.FileNotFoundException;
import java.io.FileReader;


public class Config {

    public static Config instance = new Config();

    public String zookeeper_uri;
    public int grpc_port;
    static {
        String configFile = System.getProperty("conf");
        try {
            FileReader reader = new FileReader(configFile);
            Gson gson = new Gson();
            instance = gson.fromJson(reader, Config.class);

        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}
