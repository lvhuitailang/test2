import threading
import json
import os,sys
from message import Message,MessageList


#消息接收
class MessageRev(threading.Thread):
    def __init__(self,s,root,uf,messageList):
        '''
        :param s: socket对象
        :param root: tkinter主窗口
        :param uf: 绘制的用户界面
        :param messageList: 消息列表
        '''
        threading.Thread.__init__(self)
        self.s = s
        self.root = root
        self.uf = uf
        self.messageFrame = uf.getMessageFrame()
        self.messageList = messageList
        self.start()

    def run(self):
        while True:
            try:
                revData = self.s.recv(1024).decode('utf-8')
                revMessage = json.loads(revData)
                if not revMessage or '0' == revMessage['status']:
                    print(revMessage['content'])
                    self.s.close()
                    self.root.quit()
                    sys.exit()
                elif '1' == revMessage['status']:
                    self.messageList.put(revMessage)
                    messageList = self.messageList.getMessageList()
                    [widget.destroy() for widget in self.messageFrame.winfo_children()]#清空frame
                    self.uf.flashMessage(messageList)#刷新frame
                    self.root.update()
            except Exception as e:
                print(e)
                # pass

#发送消息
class MessageSend():
    def __init__(self,s):
        self.s = s

    def send(self,messageString,status=3):
        m = Message(status=status,content=messageString)
        self.s.send(m.send())


