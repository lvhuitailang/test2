import tkinter as tk
global tk,canvas
windows = tk.Tk()
windows.title('ly')
windows.geometry('355x275')
windows.resizable(0,0)


Label1=tk.Label(windows,text="username:")
Label1.place(height = 48,width = 62,x = 26,y = 60)

Label2=tk.Label(windows,text="username:")
Label2.place(height = 48,width = 54,x = 24,y = 154)

e1 = tk.StringVar()
e2 = tk.StringVar()

Entry1=tk.Entry(windows,textvariable=e1)
Entry1.place(height = 34,width = 171,x = 119,y = 65)

Entry2=tk.Entry(windows,textvariable=e2)
Entry2.place(height = 36,width = 172,x = 118,y = 161)
e1.set('username')
e2.set('password')

def getInput():
    username = Entry1.get()
    password = Entry2.get()

    print({'username':username,'password':password})



Button1=tk.Button(windows,text="submit",command=getInput)
Button1.place(height = 30,width = 108,x = 104,y = 218)
tk.mainloop()
