import sys, os
import json
from pynput.keyboard import Controller,Key,Listener
# 监听按压
def on_press(key):
    try:
        print("正在按压:",format(key.char))
    except AttributeError:
        print("正在按压:",format(key))

# 监听释放
def on_release(key):
    print("已经释放:",format(key))
    if key==Key.esc:
        # 停止监听
        return False

    text_create(format(key))
    return format(key)
 
# 开始监听
def start_listen():
    with Listener(on_press=on_press,on_release=on_release) as listener:
        listener.join()

def text_create( msg):
    #desktop_path = "C:\\Users\\Administrator\\Desktop\\"  # 新创建的txt文件的存放路径
    full_path = 'log.txt'  #
    file = open(full_path, 'a')
    file.write(json.dumps({'name':'wolfie'}))
    file.write('\n')
    file.close()
# 循环输入监听数据到文本
# while True:
#     text_create('log', on_release(1))
#      # 这里不知道怎么把key传进去
 
if __name__ == '__main__':
 
    # 实例化键盘阿helloworld
    kb=Controller()
 
    # 开始监听,按esc退出监听
    start_listen()
