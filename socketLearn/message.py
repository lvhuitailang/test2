import json
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

    def __str__(self):
        if self.status == 1:
            return self.content
        else:
            return None,self.content
