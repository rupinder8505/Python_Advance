import threading
import time
import khrunner.main as khm
from khrunner import functions

functions.sum(2,3)

def print_time(threadName,counter,delay):
    while counter:
        time.sleep(delay)
        print(threadName + ":" + time.ctime(time.time()))
        counter =counter-1

class myThread(threading.Thread):
    def __init__(self,threadId,name,counter):
        threading.Thread.__init__(self)
        self.threadId= threadId
        self.name= name
        self.counter= counter
        
    def run(self):
        print("Starting" + self.name)
        khm.print_time(self.name,self.counter,1)
        print("Exiting"+self.name)

##print_time("Thread-1",5,1)
thread1 = myThread(1,"Thread-1",5)
thread2 = myThread(1,"Thread-2",5)
thread1.start()
thread2.start()
print("Exiting Main Thread")