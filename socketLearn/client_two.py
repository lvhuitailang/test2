#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 文件名：client.py

import socket
import json
import os,sys
import threading
import time
import tkinter as tk
from userFace import UserFace
from message import Message,MessageList
from messageSendingAndReceive import MessageRev,MessageSend



#连接服务器============
s = socket.socket()
host = '127.0.0.1'
port = 12345

# s.setblocking(False)
firstConntectTimes = time.time()
s.connect((host, port))

#创建消息对象
messageList = MessageList(10)

#创建消息发送对象
ms = MessageSend(s)

#创建用户界面
root = tk.Tk()
uf = UserFace(root,ms)

#创建消息接收线程
mr = MessageRev(s,root,uf,messageList)



root.mainloop()




