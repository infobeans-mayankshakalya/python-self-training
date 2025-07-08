from threading import *
from time import *

class MyThread:
    def counter(self):
        print(current_thread().name)
        i=0
        while(i<=10):
            sleep(1)
            print(i)
            i+=1

print(current_thread().name)
obj = MyThread()
thread = Thread(target=obj.counter)
thread.start()
sleep(1)
thread2 = Thread(target=obj.counter)
thread2.start()
sleep(1)
thread3 = Thread(target=obj.counter)
thread3.start()