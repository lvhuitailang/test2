from tkinter import *
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from faker import Faker
import random
import  os
list=(os.listdir(os.getcwd()))
'''如果文件存在图片，则先删除再重新生成'''
def delt():
    for i in list:
        if i.endswith('.png'):
            os.remove(i)
        else:
            return

def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    return (c1,c2,c3)

def getRandomText():
    '''获得随机词语'''
    global varifyCode
    f=Faker(locale='zh_CN')
    varifyCode = f.word()
    return varifyCode

def getCode():
    '''接口'''
    getRandomText()
    # 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
    image = Image.new('RGB',(80,40),getRandomColor())
    # 获取一个画笔对象，将图片对象传过去
    draw = ImageDraw.Draw(image)
    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    font=ImageFont.truetype("HanyiSentyCrayon.ttf",size=32)
    # 在图片上写东西,参数是：定位，字符串，颜色，字体
    draw.text((20,0),varifyCode,getRandomColor(),font=font)
    # 保存到硬盘，名为test.png格式为png的图片
    image.save(open(os.getcwd()+r'\\code\\test.png','wb'),'png')
    return  image
getCode()


list1=(os.listdir(os.getcwd()+r'\\code'))
def get():
    for i in list1:
        if i.endswith('.png'):
            return i
adr=(os.getcwd()+'\\code\\'+get())

master = Tk()
var = StringVar()

Label(master, text="username:").grid(sticky=E)
Label(master, text="password:").grid(sticky=E)
Label(master, text="verincode:").grid(sticky=E)
master.title('gametools')

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

def login():
    if e1.get()=="1" and e2.get() == "1"  and e3.get() == varifyCode:
        print('success')
    else:
        print('flase')
        print((e1.get()),(e2.get()),(e3.get()))

def refresh():
    '''刷新验证码'''
    getCode()
    photoTemp = PhotoImage(file=adr)
    label.configure(image = photoTemp)
    label.image = photoTemp

    pass


checkbutton = Checkbutton(master, text='Preserve aspect', variable=var)
checkbutton.grid(columnspan=2, sticky=W)

photo = PhotoImage(file=adr)
label = Label(image=photo)
label.image = photo
label.grid(row=0, column=2, columnspan=2, rowspan=2, sticky=W+E+N+S, padx=5, pady=5)

button1 = Button(master, text='Login',command=lambda:login())
button1.grid(row=2, column=2)

button2 = Button(master, text='Regist')
button2.grid(row=2, column=3)

button3 = Button(master, text='Refresh',command=lambda :refresh())
button3.grid(row=2, column=4)


mainloop()



