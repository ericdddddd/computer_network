import socket
import os

# Standard socket stuff:
host = '127.0.0.1'
port = 8000
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(5) 

# Loop forever, listening for requests:
while True:
    csock, caddr = sock.accept()
    print("Connection from: " + str(caddr))
    req = csock.recv(1024).decode()  # get the request, 1kB max
    request = req.split()[1]
    print(request)
    #print(request)
    # Look in the first line of the request for a move command
    # A move command should be e.g. 'http://server/move?a=90'
    
    if (request == '/favicon.ico'):
        continue
    elif (request == '/' or request == '/p1.html'or request == '/p2.html'):
        filename = request[1:]
        if filename == '':
            filename = 'p1.html'
        f = open(filename, 'r')
        csock.sendall(str.encode("HTTP/1.0 200 OK\n"))
        csock.sendall(str.encode('Content-Type: text/html\n'))
        csock.send(str.encode('\r\n'))
        # send data per line
        for l in f.readlines():
            #print('Sent ', repr(l))
            csock.sendall(str.encode(l))
            #l = f.read(1024)
        f.close()
        csock.close()
    else:
        csock.sendall(str.encode("HTTP/1.0 200 OK\n"))
        csock.sendall(str.encode('Content-Type: text/html\n'))
        csock.send(str.encode('\r\n'))
        csock.send(str.encode('404 NOT FOUND'))
        csock.close()