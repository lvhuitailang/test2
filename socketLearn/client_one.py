#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket
import json

from socketLearn.message import Message

s = socket.socket()         # 创建 socket 对象
host = '127.0.0.1'
port = 12345                # 设置端口号

s.connect((host, port))
while True:

    s.send('你好'.encode("utf-8"))#
    recMessage = json.loads(s.recv(1024).decode('utf-8'))
s.close()