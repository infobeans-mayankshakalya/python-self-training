import socket

host='localhost'
port=4000

s = socket.socket()
s.bind((host, port))
print('Listening on port:',port)

s.listen(1)
conn, c_addr = s.accept()

print('Connected to:',str(c_addr))

while True:
    for i in range(1, 50):
        conn.send(f"Hello, HRU? {i}".encode())
conn.close()