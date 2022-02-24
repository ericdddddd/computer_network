import argparse
import sys, time
from socket import *
import threading

BUFSIZE = 102400

port = '2000'

def server():
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('127.0.0.1', int(port)))
    s.listen(1)
    print ('Server ready...')
    receive_data_btyes = 0
    
    while 1:
        (clientsocket, address) = s.accept()
        start_time = time.time()
        
        while 1:
            data = clientsocket.recv(BUFSIZE)
            print(len(data))
            #print(data)
            #print(data)
            if not data:
                break
            else:
                #receive_data_btyes += sys.getsizeof(data)
                receive_data_btyes += len(data)
                #print(receive_data_kb)
                end_time = time.time()
            del data
            
        #print('out loop')
        clientsocket.close()
        pass_time = end_time - start_time
        receive_kb = receive_data_btyes / 1000
        print(receive_kb)
        rate = (receive_kb * 8 / 1000) / pass_time
        print('received = {} kB rate = {} Mbps'.format(int(receive_kb), rate))
        print ('Done with',address)
        receive_data_btyes = 0
        
server()