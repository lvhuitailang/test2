import tkinter as tk

root = tk.Tk()
# root.geometry('210x210+300+300')
root.resizable(0,0)
root.title('测试对话框1')
msg_frame = tk.Frame(master=root)
msg_show = tk.Label(master=root,text='哈哈哈',bg='yellow',anchor="nw", justify="left",width=30,height=10)
msg_show.grid(row=0,column=0)

input_entry = tk.Entry(master=root,width=30)
input_entry.grid(row=2,column=0)


root.mainloop()
