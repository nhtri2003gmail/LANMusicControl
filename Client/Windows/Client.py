import os
import socket
import time
import sys

import Op

PORT = 62584
HOST = ''
defGate = Op.PartGate() ## Get part of defalt gateway (192.168.xxx)

## Find which host is opening port 62584
def is_host(HOST):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(0.0015)
        s.connect((HOST, PORT))
        s.sendall(b"Welcome!")
    except:
        return False
    else:
        return True
    s.close()

## Loop from 1 to 255 (e.g: 192.168.1.xxx)
for i in range(0,256):
    if is_host(defGate + str(i)):
        HOST = defGate + str(i)
        break


#####################################################


while True:
    print('[+] Connected to server: ' + HOST)
    print()
    print("SERVER:")
    print("start: to start listening to music :D")
    print("stop : to stop completely the music")
    print("exit : to shutdown the server")
    print("CLIENT:")
    print("000  : to exit this client")
    m = input("> ")
    
    if m=='000':
        break
    if m=='' or m=='\n':
        os.system('cls')
        continue
    
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST,PORT))
            s.sendall(m.encode())
    except:
        print("Cannot connect to server!")
        print("Exiting...")
        time.sleep(1.5)
        sys.exit()
    os.system('cls')
