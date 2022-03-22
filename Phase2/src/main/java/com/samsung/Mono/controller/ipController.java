package com.samsung.Mono.controller;


import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.net.InetAddress;
import java.net.UnknownHostException;

@RestController
@RequiredArgsConstructor
@RequestMapping("/ip")
public class ipController {
    public InetAddress serverip;
    
    @RequestMapping(value="")
    public String showIp(){
        try {
            serverip = InetAddress.getLocalHost();
        } catch (UnknownHostException e) {
            e.printStackTrace();
        }
        System.out.println(serverip.toString());
        return serverip.toString();
    }
}
