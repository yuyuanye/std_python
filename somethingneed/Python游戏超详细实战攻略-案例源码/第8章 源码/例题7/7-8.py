import threading
import time
def func():
    print(time.ctime())						#打印出当前时间
print(time.ctime())
timer = threading.Timer(1, func)
timer.start() 
