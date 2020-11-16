# -*- codeing = utf-8 -*-
# @Time:2020/11/16 22:06
# @Author:Freak
# @File:threadingtest.py
# @Software:PyCharm

#threading.activeCount()的使用，此方法返回当前进程中线程的个数。返回的个数中包含主线程
#threading.enumerate()的使用。此方法返回当前运行中的Thread对象列表
#threading.setDaemon()的使用。设置后台进程(直观显示：不在控制台打印结果而在后台打印结果)
#
#调用Thread.join将会使主调线程堵塞，直到被调用线程运行结束或超时。
#参数timeout是一个数值类型，表示超时时间，如果未提供该参数，那么主调线程将一直堵塞到被调线程结束。
#
#import threading
# lock = threading.Lock()
#Lock对象
# lock.acquire()
# lock.acquire()
#产生了死琐。
# lock.release()
# lock.release()
# import threading
# rLock = threading.RLock()
#RLock对象
# rLock.acquire()
# rLock.acquire()
#在同一线程内，程序不会堵塞。
# rLock.release()
# rLock.release()
#RLock允许在同一线程中被多次acquire。而Lock却不允许这种情况。
#注意：如果使用RLock，那么acquire和release必须成对出现，即调用了n次acquire，
#必须调用n次的release才能真正释放所占用的琐。
#
#Condition.wait([timeout]):
#wait方法释放内部所占用的琐，同时线程被挂起，直至接收到通知被唤醒或超时（如果提供了timeout参数的话）。
#当线程被唤醒并重新占有琐的时候，程序才会继续执行下去。
#
#Condition.notify()
# 唤醒一个挂起的线程（如果存在挂起的线程）。注意：notify()方法不会释放所占用的琐
#Condition.notify_all()
# Condition.notifyAll()
#唤醒所有挂起的线程（如果存在挂起的线程）。注意：这些方法不会释放所占用的琐。
#
#threading.Timer
# threading.Timer是threading.Thread的子类，可以在指定时间间隔后执行某个操作
#def hello():
# print "hello, world"
# t = Timer( 3 , hello)
# t.start()
# 3秒钟之后执行hello函数。

import threading
import time
exitFlag = 0

class myThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print ("开始线程：" + self.name)
        print_time(self.name, self.counter, 5)
        print ("退出线程：" + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1

# 创建新线程
thread1 = myThread(1, "Thread-1", 1)
thread2 = myThread(2, "Thread-2", 1)

# 开启新线程
thread1.start()
thread2.start()
print ("current has %d threads"%(threading.active_count()-1))
thread1.join()
thread2.join()
print ("退出主线程")
