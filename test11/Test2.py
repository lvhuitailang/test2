from tkinter import *

#encoding=utf-8
import tkinter
import tkinter.messagebox
import webbrowser
from PIL import Image,ImageTk

def vip():

    def Button():
        a = 'http://55jx.top/?url=' if varRadio.get() else 'http://mimijiexi.top/?url='
        b = entry_movie_link.get()
        webbrowser.open(a+b)
    def qk():
        entry_movie_link.delete(0,'end')

    def openaqy():
        webbrowser.open('http://www.iqiyi.com')

    def opentx():
        webbrowser.open('http://v.qq.com')

    def openyq():
        webbrowser.open('http://www.youku.com/')

    def openbz():
        webbrowser.open('https://www.bilibili.com/')


    root=tkinter.Tk()
    root.title('VIPmovie1.0')
    root['width']=500
    root['height']=300
    root.resizable(width=False,height=False)


    menubar = tkinter.Menu(root)
    helpmenu = tkinter.Menu(menubar, tearoff=0)
    root.config(menu=menubar)

    varentry1= tkinter.StringVar(value='')
    lab_movie_gallery=tkinter.Label(root, text='接口：')
    lab_movie_gallery.place(x=20,y=20,width=100,height=20)
    varRadio=tkinter.IntVar(value=1)
    Radiobutton1_movie_gallery=tkinter.Radiobutton(root,variable=varRadio,value=0,text='接口1')
    Radiobutton2_movie_gallery = tkinter.Radiobutton(root, variable=varRadio, value=1, text='接口2')
    Radiobutton1_movie_gallery.place(x=130,y=20,width=100,height=20)
    Radiobutton2_movie_gallery.place(x=250, y=20, width=100, height=20)

    varentry2=tkinter.StringVar(value='这里放入视频URL地址')
    lab_movie_link = tkinter.Label(root, text='URL：')
    lab_movie_link.place(x=20, y=60, width=100, height=20)
    entry_movie_link = tkinter.Entry(root, textvariable=varentry2)
    entry_movie_link.place(x=130, y=60, width=300, height=20)
    button_movie_link=tkinter.Button(root,text='清空',command=qk)
    button_movie_link.place(x=440,y=60,width=40,height=20)
    lab_remind = tkinter.Label(root, text='')
    lab_remind.place(x=50, y=90, width=400, height=20)
    varbutton=tkinter.StringVar
    button_movie= tkinter.Button(root, text='播放', command=Button)
    button_movie.place(x=140, y=120, width=200, height=60)

    button_movie1 = tkinter.Button(root, text='爱奇艺', command=openaqy)
    button_movie1.place(x=30, y=200, width=70, height=60)

    button_movie2 = tkinter.Button(root, text='腾讯视频', command=opentx)
    button_movie2.place(x=110, y=200, width=70, height=60)

    button_movie3 = tkinter.Button(root, text='优酷视频', command=openyq)
    button_movie3.place(x=190, y=200, width=70, height=60)

    button_movie4 = tkinter.Button(root, text='bilibili', command=openbz)
    button_movie4.place(x=270, y=200, width=70, height=60)

    button_movie4 = tkinter.Button(root, text='待添加')
    button_movie4.place(x=350, y=200, width=90, height=60)

    button_movie4 = tkinter.Label(root)
    button_movie4.place(x=50, y=270, width=400, height=50)

    root.mainloop()


master = Tk()
var = StringVar()

Label(master, text="username:").grid(sticky=E)
Label(master, text="password:").grid(sticky=E)
master.title('gametools')

u=StringVar()
p=StringVar()


e1 = Entry(master, textvariable=u)
e2 = Entry(master,textvariable=p)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
def get():
    if u.get()=='admin' and p.get() == 'admin' :
        master.destroy()
        vip()

        return
    else:
        master.title('账号密码错误')

checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
checkbutton.grid(columnspan=2, sticky=W)

# photo = PhotoImage(file='3.png')
label = Label()
label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

button1 = Button(master, text='Login',command= lambda:get())
button1.grid(row=2, column=2)

button2 = Button(master, text='Regist')
button2.grid(row=2, column=3)


mainloop()



