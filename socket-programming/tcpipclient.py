import socket

s = socket.socket()

s.connect(('localhost', 4000))

msg = s.recv(1024)

while msg:
    print('Message:', msg.decode())
    msg = msg.recv(1024)

s.close()