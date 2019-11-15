import tkinter as tk

root = tk.Tk()
# root.geometry('200x200+300+300')
# root.resizable(0,0)
root.title('测试对话框1')
msg_frame = tk.Frame(bg='yellow',width=200, height=320)
msg_frame.grid(row=0,column=0,sticky=tk.W+tk.N)#消息框frame
input_frame = tk.Frame(width=200,height=10)
input_frame.grid(row=1,column=0)#输入框frame

right_frame = tk.Frame(master=root,width=0,height=330)
right_frame.grid(row=0,column=1,rowspan=2)


msg_show = tk.Label(master=msg_frame,text='哈哈哈',bg='pink',anchor="nw", justify="left",width=30)
input_entry = tk.Entry(master=input_frame,width=30)
msg_show.grid(row=0,column=0)
input_entry.grid(row=0,column=0)

root.mainloop()
