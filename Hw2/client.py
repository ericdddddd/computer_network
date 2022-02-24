import sys, time
from socket import *

def client():
    count = 0
    BUFSIZE = 102400 # 1KB
    ip = '127.0.0.1'
    port = '2000'
    data = '0' * (1000-1) + '\n'
    print(len(data))
    t1 = time.time()
    clientSocket = socket(AF_INET, SOCK_STREAM)
    t2 = time.time()
    clientSocket.connect((ip, int(port)))
    t3 = time.time()
    t4 = time.time()
    while (t4 - t3 < 1):
        #s.send(bytearray(testdata,"utf-8"))
        count += 1
        return_v = clientSocket.send(bytearray(data,"utf-8"))
        print(return_v)
        t4 = time.time()
        #return_data = clientSocket.recv(BUFSIZE)
    
    clientSocket.close()
    #print ('ping:', (t3-t2)+(t5-t4)/2)
    print ('Time:', t4-t3)
    sent_kb = count
    sent_mb = sent_kb / 1000
    rate = sent_mb * 8 / 1
    print('sent = {} kB rate = {} Mbps'.format(sent_kb, rate)) 
    #print ('Bandwidth:', round((BUFSIZE*count*0.001) / (t4-t3), 3),)
    #print ('Kb/sec.')
    
client()