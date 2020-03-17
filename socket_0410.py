import socket
host = '127.0.0.1'
port = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(5)
conn, addr = s.accept()
print 'Connect by', addr
while True:
    data = conn.recv(1024)
    if not data:
        break
    print data
    conn.sendall(data)
