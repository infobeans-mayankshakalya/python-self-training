import threading

print(threading.current_thread().name)
if(threading.current_thread().name == threading.main_thread()):
    print('Main Thread is running')
else:
    print('Some other child thread is running')