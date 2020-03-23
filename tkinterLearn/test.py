import threading
import time
import tkinter as tk



class UserFace(threading.Thread):
    def __init__(self,root):
        threading.Thread.__init__(self)
        self.root = root
        self.start()

    def run(self):
        aa = input()

root = tk.Tk()
root.geometry('200x200')
root.title('测试窗口')
btn = tk.Button(master=root,text='click Me!')
btn.grid(sticky=tk.EW)
a = UserFace(root)
root.mainloop()
