import json
import tkinter as tk
'''
    0：服务端发送错误信息给客户端 
    1:服务端发送正常信息给客户端 
    2:客户端向服务端注册名字
    3:客户端发送正常信息给服务端

'''
class Message:

    status = 1
    content = None
    def __init__(self,status=1,content=''):
        self.status = status
        self.content = content
        pass
    def send(self):
        json_str = {'status':str(self.status),'content':self.content}
        return json.dumps(json_str).encode('utf-8')



class MessageList():
    def __init__(self,maxMessageNum):
        self.maxMessageNum = maxMessageNum
        self.messageList = list()

    #存放消息
    def put(self,messageDic):
        if len(self.messageList)>=self.maxMessageNum:
            self.messageList.pop(0)

        messageObj = Message(status=messageDic['status'],content=messageDic['content'])
        self.messageList.append(messageObj)

    #获得消息Lable列表
    def getMessageList(self):
        return self.messageList
