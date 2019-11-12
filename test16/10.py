from queue import Queue
import time
import threading
import queue

q = queue.Queue(maxsize=10)

class Tt(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        while True:
            a = input('a:')
            q.put(a)

if __name__ == '__main__':
    t = Tt()
    t.start()
    while True:
        try:
            print(q.get_nowait())
        except Exception as e:
            pass


