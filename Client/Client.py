import os
import socket
import time
import sys

import Op

PORT = 62584
HOST = ''
defGate = Op.PartGate()

def is_host(HOST):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(0.00015)
        s.connect((HOST, PORT))
        s.sendall(b"Hello Johnathan Huu Tri!")
    except:
        return False
    else:
        return True
    s.close()

for i in range(0,256):
    if is_host(defGate + str(i)):
        HOST = defGate + str(i)
        break

print('[+] Connected to server: ' + HOST)
print()

while True:
    print("SERVER:")
    print("start: to start listening to music :D")
    print("stop : to stop completely the music")
    print("exit : to shutdown the server")
    print("CLIENT:")
    print("000  : to exit this client")
    m = input("Message: ")
    
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
