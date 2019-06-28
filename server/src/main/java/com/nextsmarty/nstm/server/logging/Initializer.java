package com.nextsmarty.nstm.server.logging;

import io.netty.channel.ChannelInitializer;
import io.netty.channel.ChannelPipeline;
import io.netty.channel.socket.SocketChannel;
import io.netty.handler.codec.http.*;

public class Initializer extends ChannelInitializer<SocketChannel> {

    @Override
    public void initChannel(SocketChannel ch) {
        ChannelPipeline p = ch.pipeline();

        // HttpServerCodec is a combination of HttpRequestDecoder and HttpResponseEncoder
        p.addLast(new HttpServerCodec());

        p.addLast(new HttpObjectAggregator(1048576));

        p.addLast(new Handler());
    }
}