import tkinter as tk
windows = tk.Tk()
windows.title('ly')
windows.geometry('355x275')
windows.resizable(0,0)

Label1=tk.Label(windows,text='     username:')
Label1.place(height = 48,width = 62,x = 26,y = 60)

Label2=tk.Label(windows,text='key:')
Label2.place(height = 48,width = 54,x = 24,y = 154)

u=tk.StringVar()
p=tk.StringVar()

Entry1=tk.Entry(windows,textvariable=u)
Entry1.place(height = 34,width = 171,x = 119,y = 65)

Entry2=tk.Entry(windows,textvariable=p)
Entry2.place(height = 36,width = 172,x = 118,y = 161)

def succes():
    successWindows = tk.Toplevel()
    successWindows.geometry('86x55')
    successWindows.resizable(0,0)
    var=tk.StringVar()
    e =tk.Entry(successWindows, textvariable = var,state='readonly')
    var.set('success')
    e.pack()
    successWindows.mainloop()

def flas():
    import tkinter as tk
    windows = tk.Tk()
    windows.geometry('86x55')
    windows.resizable(0,0)
    var=tk.StringVar()
    e =tk.Entry(windows, textvariable = var,state='readonly')
    var.set('flase')
    e.pack()
    tk.mainloop()

u.set('输入账号')
p.set('输入密码')
def get():
    username=u.get()
    password=p.get()
    if username=='123' and password=='456':
       succes()
    else:
        flas()



Button1=tk.Button(windows,text='login',command=get)
Button1.place(height = 30,width = 108,x = 104,y = 218)
tk.mainloop()
