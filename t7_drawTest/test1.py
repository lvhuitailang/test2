import tkinter as tk

canvas_width = 200
canvas_height = 200

class MyOval:
    def __init__(self,canvas,shapeTag,x1,y1,x2,y2,ovalParam):
        self.canvas = canvas
        self.shapeTag = shapeTag
        self.ovalParam = ovalParam
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def moveTo(self,x1,y1,x2,y2):
        #清除形状
        canvas.delete(self.shapeTag)

        #处理参数
        if x1 is not None:
            self.x1 += x1
            # adjust max value
            if self.x1 <= 0:
                self.x1 = 0
                self.x2 = 50

        if y1 is not None:
            self.y1 += y1
            # 调整边缘最大值
            if self.y1 <= 0:
                self.y1 = 0
                self.y2 = 50

        if x2 is not None:
            self.x2 += x2
            # 调整边缘最大值
            if self.x2 >= canvas_width:
                self.x2 = canvas_width
                self.x1 = canvas_width - 50
        if y2 is not None:
            self.y2 += y2
            # adjust max value
            if self.y2 >= canvas_height:
                self.y2 = canvas_height
                self.y1 = canvas_height - 50









        #重新创建形状
        canvas.create_oval(self.x1,self.y1,self.x2,self.y2,ovalParam)








#window对象
window = tk.Tk()
window.title('test drawing')
window.resizable(0, 0)
#window size
window.geometry(str(canvas_width)+'x'+str(canvas_height))


#canvas 对象
canvas = tk.Canvas(window,width=canvas_width,height=canvas_height,bg='#f00',cursor='circle')
canvas.pack()
#画圆
ovalParam = {'fill':'#fff','tags':'oval1'}
oval = canvas.create_oval(0,0,50,50,ovalParam)

myOvalObj = MyOval(canvas = canvas,shapeTag = 'oval1',x1=0,y1=0,x2=50,y2=50,ovalParam=ovalParam)



#事件处理方法
def printKey(key):
    print(key.keycode)

    x1 = None
    y1 = None
    x2 = None
    y2 = None
    keycode = key.keycode
    if 38 == keycode:
        y1 = -2
        y2 = -2
        window.title('上移')
    elif 40 == keycode:
        y1 = 2
        y2 = 2
        window.title('下移')
    elif 37 == keycode:
        x1 = -2
        x2 = -2
        window.title('左移')
    elif 39 == keycode:
        x1 = 2
        x2 = 2
        window.title('右移')
    myOvalObj.moveTo(x1,y1,x2,y2)



    print(keycode)

#事件绑定
window.bind('<Key>',printKey)

window.mainloop()