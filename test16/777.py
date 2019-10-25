import random
from tkinter import *
class App(Frame):
    def __init__(self):
        super(App, self).__init__()
        self.initWidgets()
    def initWidgets(self):
        #定义字符串元组
        books=('疯狂Python讲义', '疯狂Swift讲义', '疯狂Kotlin讲义', \
               '疯狂Java讲义', '疯狂Ruby讲义')
        for i in range(len(books)):
            #生成三个随机数
            ct = [random.randrange(256) for x in range(3)]
            grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
            # 将元组中3个随机数格式化成16进制数,转成颜色格式
            bg_color = "#%02x%02x%02x" % tuple(ct)
            #创建Label,设置背景色和前景色
            lb = Label(self.master,
                       text=books[i],
                       fg='White' if grayness < 120 else 'Black',
                       bg=bg_color)
            # 使用place()设置该Label的大小和位置
            lb.place(x=20, y=36 + i * 36, width=180, height=30)
app=App()
app.master.title('Place布局')
app.master.geometry('250x250+30+30')
app.mainloop()