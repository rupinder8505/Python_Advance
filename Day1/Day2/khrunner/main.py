import time
def print_time(threadName,counter,delay):
    while counter:
        time.sleep(delay)
        print(threadName + ":" + time.ctime(time.time()))
        counter =counter-1