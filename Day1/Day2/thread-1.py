import time 
import threading
def task():
    time.sleep(1)
    print("This is long task")

print("Hello")

threading.Thread(target = task).start



print("Bye")