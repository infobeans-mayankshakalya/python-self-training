import random
from  time import *
import queue
from threading import *

def Producer(q):
    while True:
        print('Producing')
        q.put(random.randint(1,50))
        print('Produced')
        sleep(3)

def Consumer(q):
    while True:
        print('Ready to consume')
        print('Consumed data:', q.get())
        sleep(3)

q = queue.Queue()
t1 = Thread(target=Consumer, args=(q,))
t2 = Thread(target=Producer, args=(q,))

t1.start()
t2.start()