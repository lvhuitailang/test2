import tkinter as tk


class UserFace():
    def __init__(self,root,ms):
        self.ms = ms
        self.root = root
        self.root.geometry('400x400+300+300')
        self.inputStr = tk.StringVar()
        self.drawUI()

    def drawUI(self):
        self.root.title('测试对话框1')
        self.messageFrame = tk.Frame(bg='yellow',width=400, height=320,padx=2,pady=2)#消息框frame
        frame_l_bottom = tk.Frame(width=400,height=80,padx=2,pady=2)#输入框frame
        self.messageFrame.grid(row=0,column=0,sticky=tk.NW)
        frame_l_bottom.grid(row=1,column=0,sticky=tk.SW)

        self.messageFrame.grid_propagate(False)
        frame_l_bottom.grid_propagate(False)

        input_entry = tk.Entry(master=frame_l_bottom,width=35,textvariable =self.inputStr)
        send_btn = tk.Button(master=frame_l_bottom,text='Send',width=20,height=5,command=lambda :self.sendBtn(input_entry))

        input_entry.grid(row=0,column=0,sticky=tk.NS)
        send_btn.grid(row=0,column=1)
        self.root.update()

    def getMessageFrame(self):
        return self.messageFrame

    def flashMessage(self,messageList):
        for perMessage in messageList:
            lableObj = tk.Label(master=self.messageFrame,text=perMessage.content,bg='pink',anchor="nw", justify="left",width=60)
            lableObj.grid()

    def sendBtn(self,input_entry):
        self.ms.send(input_entry.get())
        self.inputStr.set('')

