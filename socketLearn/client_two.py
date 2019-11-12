#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket
from socketLearn.message import Message


s = socket.socket()         # 创建 socket 对象
host = '127.0.0.1'
port = 12345                # 设置端口号

s.connect((host, port))
print(s.recv(1024).decode('utf-8'))
s.close()