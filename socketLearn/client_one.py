#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket
import json
import os,sys
import threading
from message import Message

class MessageRev(threading.Thread):
    def __init__(self,s):
        threading.Thread.__init__(self)
        self.s = s

    def run(self):
        while True:
            msg = input('请输入聊天内容: ')
            m = Message(status=3,content=msg)
            s.send(m.send())




s = socket.socket()         # 创建 socket 对象
host = '127.0.0.1'
port = 12345                # 设置端口号
s.setblocking(False)
try:
    s.connect((host, port))
except Exception as e:
    pass
try:
    revData = s.recv(1024).decode('utf-8')
    revMessage = json.loads(revData)
    if not revMessage or '0' == revMessage['status']:
        print(revMessage['content'])
        s.close()
        sys.exit()
    elif '1' == revMessage['status']:
        print(revMessage['content'])
except Exception as e:
    pass

mr = MessageRev(s)
mr.start()
try:
    while True:
        revData = s.recv(1024).decode('utf-8')
        revMessage = json.loads(revData)
        if not revMessage or '0' == revMessage['status']:
            print(revMessage['content'])
            s.close()
            break;
        elif '1' == revMessage['status']:
            print(revMessage['content'])
except BlockingIOError as be:
    pass
