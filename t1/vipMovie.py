#encoding=utf-8
import tkinter
import tkinter.messagebox
import webbrowser
from PIL import Image,ImageTk

def vip():
    entry_movie_link = None
    varRadio = None

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

    def opensuge():
        webbrowser.open('http://www.z7yy.com/')


    root=tkinter.Tk()
    root.title('VIPmovie1.0')
    # Canvas=tkinter.Canvas(root,width=500,height=300,bd=0, highlightthickness=0)
    # imgpath='3.gif'
    # img=Image.open(imgpath)
    # photo=ImageTk.PhotoImage(img)
    # Canvas.create_image(0,0,image=photo)
    # Canvas.pack()
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

    varentry2=tkinter.StringVar(value='这里放入视频URL')
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

    button_movie4 = tkinter.Button(root, text='苏格影院', command=opensuge)
    button_movie4.place(x=350, y=200, width=90, height=60)

    button_movie4 = tkinter.Label(root, text='bug反馈163邮箱：hx@163.com')
    button_movie4.place(x=50, y=270, width=400, height=50)

    root.mainloop()


