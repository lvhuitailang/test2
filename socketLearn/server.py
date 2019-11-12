#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：server.py

import socket
import json
from socketLearn.message import Message

MAX_CLIENTNUM = 1
clients = {}

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setblocking(False)
host = '0.0.0.0'
port = 12345                # 设置端口
s.bind((host, port))        # 绑定端口
s.listen(MAX_CLIENTNUM)                 # 等待客户端连接
while True:
    try:
        c,addr = s.accept()     # 建立客户端连接
        nameKey = addr[0]+':'+str(addr[1])
        recMessage = json.loads(s.recv(1024).decode('utf-8'))
        if '2' == recMessage.status:
            #客户端注册
            if (len(clients) < MAX_CLIENTNUM) and (not clients.get(nameKey)) :
                clients[nameKey] = c
                m = Message(1,'连接成功')
                c.send(m.send())
            else:
                m = Message(0,'客户端数量超限，抱歉')
                c.send(m.send())
                c.close()
                continue
        elif '3' == recMessage.status:
            #客户端发消息
            c = clients.get(nameKey)
            if not c:
                m = Message(0,'你没有注册，抱歉')
                c.send(m.send())
                c.close()
                continue
            else:
                #发送给所有客户端
                for key,val in clients.items():
                    m = Message(1,key+' 说:'+recMessage.content)
                    val.send(m.send())
                    continue
        else:
            continue






        print('连接地址：', addr)

    except BlockingIOError as bioe:
        pass