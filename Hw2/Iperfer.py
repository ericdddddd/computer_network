import sys, time
from socket import *
import threading
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="computer network Hw2")
    parser.add_argument("-C", '--client', action="store_true", help="clients evaluation")
    parser.add_argument("-S", '--server', action="store_true", help="server evaluation")
    parser.add_argument("-H", '--host',  type = str, help="server IP")
    parser.add_argument("-P", '--port',  type = int, help="server port")
    parser.add_argument("-T", '--time',  type = float, help="time")
    args = parser.parse_args()
    return args
    
def server(port):

    BUFSIZE = 102400
    s = socket(AF_INET, SOCK_STREAM)
    s.bind(('', int(port))) # ''不指定IP，則選取目前的電腦使用的IP
    s.listen(1)
    print ('Server ready...')
    receive_data_btyes = 0
    
    while True:
        (clientsocket, address) = s.accept()
        start_time = time.time()
        
        while True:
            data = clientsocket.recv(BUFSIZE)
            #print(sys.getsizeof(data))
            if not data:
                break
            else:
                receive_data_btyes += len(data)
                #receive_data_btyes += 1000
                end_time = time.time()
            del data
            
        clientsocket.close()
        pass_time = end_time - start_time
        receive_kb = receive_data_btyes / 1000
        rate = (receive_kb * 8 / 1000) / pass_time
        print('received = {} kB rate = {} Mbps'.format(int(receive_kb), rate))
        #print ('Done with',address)
        receive_data_btyes = 0
        
def client(ip,port,target_time):

    send_bytes = 0
    BUFSIZE = 102400 
    data = '0' * (1000-1) + '\n' # 1KB
    
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((ip, int(port)))
    
    start_time = time.time()
    end_time = time.time()
    
    while (end_time - start_time < target_time):
    
        btyes = clientSocket.send(bytearray(data,"utf-8"))
        send_bytes += btyes # send data + 1KB
        #print(data)
        end_time = time.time()
    
    clientSocket.close()
    #print ('Time:', end_time - start_time)
    sent_kb = send_bytes / 1000
    sent_mb = sent_kb / 1000
    rate = sent_mb * 8 / target_time
    print('sent = {} kB rate = {} Mbps'.format(sent_kb, rate)) 

def miss_argument():
    print('Error: missing or additional arguments')
def error_port():
    print('Error: port number must be in the range 1024 to 65535')
    
def main(args):
    #print(args)
    if(args.client == True and args.server == True):
        miss_argument()
        
    elif(args.client):
        port = args.port
        if (args.host == None or args.port == None or args.time == None):
            miss_argument()
        elif (port < 1024 or port > 65535):
            error_port()
        else:
            ip = args.host
            target_time = args.time
            #print(1)
            client(ip , port ,target_time)
            
    elif(args.server):
        if (args.host == None or args.time == None):
            port = args.port
            if (port == None):
                port = 0
            if (port < 1024 or port > 65535):
                error_port()
            else:
                #print(1)
                server(port)
        else:
            miss_argument()
    else:
        miss_argument()
     
if __name__ == "__main__":
    """
    try:
        args = parse_args()
        main(args)
    
    except:
        print('Error: missing or additional arguments')
        
    """
    args = parse_args()
    main(args)

 


