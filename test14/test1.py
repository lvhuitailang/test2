import tkinter as tk

root = tk.Tk()

var1 = tk.IntVar()
root.title = '测试'
root.geometry("300x300")
root.wm_attributes('-topmost',1)#置顶
root.attributes("-alpha",0.9)#透明
# root.resizable(width=False,height=False)


tk.Label(root,text='first').grid(row=0,sticky=tk.E)
tk.Label(root,text='second').grid(row=1,sticky=tk.E)

tk.Entry(root).grid(row=0,column=1)
tk.Entry(root).grid(row=1,column=1)

tk.Checkbutton(root,text='remember Me',variable=var1).grid(row=3,columnspan=2,sticky=tk.W)

phpto = tk.PhotoImage(file='img/fy.gif')
logo = tk.Label(image=phpto)
logo.image=phpto
logo.grid(row=0,column=2,rowspan=2,columnspan=2,sticky=tk.W+tk.E+tk.N+tk.S, padx=5, pady=5)




root.mainloop()