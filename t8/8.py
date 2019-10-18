import sys, time,os


percent = 0.0
progressBlock = '█'
progressBar = ''
for i in range(20):

    sys.stdout.write(progressBlock)
    sys.stdout.flush()
    os.system('cls')
    time.sleep(1)