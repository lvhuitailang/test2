import tkinter as tk
import threading
import time

root = tk.Tk()
root.geometry('400x400+300+300')
# root.resizable(0,0)

root.title('测试对话框1')
frame_l_top = tk.Frame(bg='yellow',width=400, height=320,padx=2,pady=2)#消息框frame
frame_l_bottom = tk.Frame(width=400,height=80,padx=2,pady=2)#输入框frame
frame_l_top.grid(row=0,column=0,sticky=tk.NW)
frame_l_bottom.grid(row=1,column=0,sticky=tk.SW)

frame_l_top.grid_propagate(False)
frame_l_bottom.grid_propagate(False)


msg_show = tk.Label(master=frame_l_top,text='哈哈哈',bg='pink',anchor="nw", justify="left",width=60)
msg_show_2 = tk.Label(master=frame_l_top,text='哈哈哈2',bg='pink',anchor="nw", justify="left",width=60)
input_entry = tk.Entry(master=frame_l_bottom,width=35)
send_btn = tk.Button(master=frame_l_bottom,text='Send',width=20,height=5,command=lambda :loogFun(10))

msg_show.grid(row=0,column=0)
msg_show_2.grid(row=1,column=0)
input_entry.grid(row=0,column=0,sticky=tk.NS)
send_btn.grid(row=0,column=1)

def loogFun(num):
    while num > 0:
        print(num)
        num -=1
        time.sleep(1)


if __name__ == '__main__':

    root.mainloop()

