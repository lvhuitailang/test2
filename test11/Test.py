from tkinter import *

master = Tk()
var = StringVar()

Label(master, text="username:").grid(sticky=E)
Label(master, text="password:").grid(sticky=E)
master.title('gametools')

u=StringVar()
p=StringVar()


e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)


checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
checkbutton.grid(columnspan=2, sticky=W)


label = Label()

label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

button1 = Button(master, text='Login',command=lambda :getUsername(e1))
button1.grid(row=2, column=2)

button2 = Button(master, text='Regist')
button2.grid(row=2, column=3)

def getUsername(e):
    print(e.get())
    master.destroy()

mainloop()



