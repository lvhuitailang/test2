import tkinter as tkinter
import pyeputLearn.test1 as tt
import time

window = tkinter.Tk()
window.title = '测试'
window.geometry("300x300")
window.wm_attributes('-topmost',1)#置顶
window.attributes("-alpha",0.9)#透明

window.resizable(width=False,height=False)


listener = tt.MyListener()

# 记录
def redord():
    filepath = 'file.txt'
    with open(filepath,'r+') as f:
        f.truncate()
    listener.startListen()

# 停止记录
def stopRecord():
    listener.stopListen()

# 回放
def play():
    time.sleep(2)
    doEvent = tt.DoEvent()
    eventList = doEvent.readFile()
    doEvent.doEvent(eventList)



tkinter.Button(window,text='记录',command=lambda :redord()).pack(side='top')
tkinter.Button(window,text='停止记录',command=lambda :stopRecord()).pack(side='top')
tkinter.Label(window,text="按esc停止记录").pack(side='top')
tkinter.Button(window,text='回放',command=lambda :play()).pack(side='bottom')
tkinter.Button(window,text='退出程序',command=window.quit).pack(side='bottom')


window.mainloop()
