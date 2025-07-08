from threading import *

class Book:
    def __init__(self, availableSeats):
        self.availableSeats = availableSeats
        self.l = Semaphore()
    def buy(self, seats):
        print('Thread: ', current_thread().name)
        print('Available seats: ', self.availableSeats)
        self.l.acquire()
        if(self.availableSeats>=seats):
            print('Confirming Booking...')
            print('Processing Payment...')
            print('Print the Ticket...')
            self.availableSeats -= seats
        else:
            print('No seats available')
        self.l.release()

obj = Book(10)
t1 = Thread(target=obj.buy, args=(3,))
t2 = Thread(target=obj.buy, args=(4,))
t3 = Thread(target=obj.buy, args=(3,))
t4 = Thread(target=obj.buy, args=(2,))

t1.start()
t2.start()
t3.start()
t4.start()