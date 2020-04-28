import os
import random
import time
import socket
from playsound import playsound

HOST = '127.0.0.1'
PORT = 62584

with open('server.conf', 'rt') as f:
    path = f.read()
    
try:
    playlist = os.listdir(path)
except:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall("Cannot find the Music Folder!".encode())
    sys.exit()

os.chdir(path)

while True:
    filename = str(playlist[random.randrange(0,len(playlist))]) ## e.g: len=25 ==> 0->24
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            s.sendall(filename.encode())
    except:
        sys.exit()
    playsound(f'{path}\\{filename}')
    time.sleep(random.randrange(1,3)) ## Break for a while before turning to another song
