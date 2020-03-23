import threading

if __name__ == '__main__':
    for num in range(100000):
        threading.Thread(target=lambda :print('第'+str(num)+'个线程。')).start()
