import os
import socket
import time
import sys

try:
    with open('client.conf', 'rt') as f:
        HOST = f.read()
except:
    print("Cannot find client.conf!")
    print('Exiting...')
    time.sleep(1.5)
    sys.exit()

PORT = 62584

while True:
    print("start: to start listening to music :D")
    print("stop : to stop completely the music")
    print("exit : to shutdown the server")
    print()
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
