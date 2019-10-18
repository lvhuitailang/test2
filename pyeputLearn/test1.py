from pynput import mouse,keyboard
import time
import json
import sys



class Event:
    '''事件对象'''
    # 初始化
    def __init__(self,source,event,target,location,keyChar):
        '''
        source:源，比如 键盘，鼠标
        event:事件，比如 click，press，release,move,scroll
        target:目标，比如 Button.left，c,shift的vk值
        location:坐标，鼠标的话有坐标 x，y
        keyChar:键字符

        '''

        eventObj = dict()
        eventObj['source'] = source
        eventObj['event'] = event
        eventObj['target'] = target
        eventObj['location'] = location
        eventObj['keyChar'] = keyChar
        self.eventObj = eventObj

    def getEventObj(self):
        return self.eventObj

    # 写入文件
    def writeToFile(self):
        filepath = 'file.txt'
        with open(filepath,'a',encoding='utf-8') as f:
            f.writelines(json.dumps(self.eventObj)+'\n')



class MyListener:
    '''监听对象'''
    def __init__(self):
        pass

    # 鼠标移动事件
    def mouse_move(self,x, y):
        # print('[Move]', (x, y))
        Event('mouse','move',None,{'x':x,'y':y},None).writeToFile()
    # 鼠标点击事件
    def mouse_click(self,x, y, button, pressed):
        Event('mouse','press' if pressed else 'release',button.name,{'x':x,'y':y},None).writeToFile()
        # print('[Click]', (x, y, button.name, pressed))

    # 鼠标滚动事件
    def mouse_scroll(self,x, y, x_axis, y_axis):
        # print('[Scroll]', (x, y, x_axis, y_axis))
        Event('mouse','scroll',None,{'x':x,'y':y,'x_axis':x_axis,'y_axis':y_axis},None).writeToFile()

    # 键盘按下事件
    def keyboard_press(self,key):
        if key == keyboard.Key.esc:
            print(1)
            # 停止监听
            self.stopListen()
            return False
        try:
            Event('keyboard','press',key.vk,None,key.char).writeToFile()
        except AttributeError:
            try:
                Event('keyboard','press',key.value.vk,None,'').writeToFile()
            except AttributeError:
                Event('keyboard','press',key.vk,None,'').writeToFile()


# 按键释放监听
    def keyboard_release(self,key):
        # if key == keyboard.Key.backspace:
        #     # 开始回放监听
        #     time.sleep(2)
        #     doEvent = MyListener.DoEvent()
        #     eventList = doEvent.readFile()
        #     doEvent.doEvent(eventList)
        #     return True
        try:
            Event('keyboard','release',key.vk,None,key.char).writeToFile()
        except AttributeError:
            try:
                Event('keyboard','release',key.value.vk,None,'').writeToFile()
            except AttributeError:
                Event('keyboard','release',key.vk,None,'').writeToFile()


    # 初始化鼠标事件监听
    def initMouseListen(self):
        self.mouseListener = mouse.Listener(on_move=self.mouse_move, on_click=self.mouse_click, on_scroll=self.mouse_scroll )

    # 初始化键盘事件监听
    def initKeyboardListen(self):
        self.keyboardListener = keyboard.Listener(on_press=self.keyboard_press,on_release=self.keyboard_release)

    # 开始监听
    def startListen(self):
        try:
            self.mouseListener.start()
            self.keyboardListener.start()
            # self.mouseListener.join()
            # self.keyboardListener.join()
        except AttributeError:
            self.initMouseListen()
            self.initKeyboardListen()
            self.mouseListener.start()
            self.keyboardListener.start()
            # self.mouseListener.join()
            # self.keyboardListener.join()
        return self

    # 结束监听
    def stopListen(self):
        self.keyboardListener.stop()
        self.mouseListener.stop()


class DoEvent:
    eventList = list()
    '''事件读取执行'''
    def __init__(self):
        self.keyBoard = keyboard.Controller()
        self.mouse = mouse.Controller()

    #读取事件文件,返回事件对象集合
    def readFile(self):
        with open('file.txt','r') as f:
            eventString = f.readline()
            while eventString:
                eventItem = json.loads(eventString)
                self.eventList.append(eventItem)
                eventString = f.readline()
        return self.eventList

    # 执行事件
    def doEvent(self,eventList):
        if eventList is None:
            eventList = self.eventList

        for eventItem in eventList:
            if 'keyboard' == eventItem['source']:
                self.doKeyboardEvent(eventItem)
            elif 'mouse' == eventItem['source']:
                self.doMouseEvent(eventItem)
            time.sleep(0.01)


    # 执行键盘事件
    def doKeyboardEvent(self,eventItem):
        event = eventItem['event']
        vk = keyboard.KeyCode.from_vk(eventItem['target'])
        if 'press' == event:
            self.keyBoard.press(vk)
        elif 'release' == event:
            self.keyBoard.release(vk)

    # 执行鼠标事件
    def doMouseEvent(self,eventItem):
        event = eventItem['event']
        # 按下
        if 'press' == event:
            # position = eventItem['location']
            # self.mouse.move(**position)
            if 'left' == eventItem['target']:
                self.mouse.press(mouse.Button.left)
            elif 'right' == eventItem['target']:
                self.mouse.press(mouse.Button.right)
            elif 'middle' == eventItem['target']:
                self.mouse.press(mouse.Button.middle)

        # 抬起
        elif 'release' == event:
            # position = eventItem['location']
            if 'left' == eventItem['target']:
                self.mouse.release(mouse.Button.left)
            elif 'right' == eventItem['target']:
                self.mouse.release(mouse.Button.right)
            elif 'middle' == eventItem['target']:
                self.mouse.release(mouse.Button.middle)
        # 移动
        elif 'move' == event:
            position = eventItem['location']
            self.mouse.position = (position['x'],position['y'])
        # 滚动
        elif 'scroll' == event:
            position = eventItem['location']
            self.mouse.scroll(**position)



if __name__=='__main__':
    # doEvent = DoEvent()
    # eventList = doEvent.readFile()
    # doEvent.doEvent(eventList)
    listener = MyListener().startListen()
    # startListen()
    #  mouse = Controller()
    #  time.sleep(5)
    #  for index in range(10):
    #      mouse.press(Button.left)
    #      mouse.move(index,-index)
    #      time.sleep(1)
    #writeToFile(1)
    pass