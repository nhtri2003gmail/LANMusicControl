import socket
import os
import time

HOST = '0.0.0.0'
PORT = 62584

print('[+] Server started successfully')
print('[+] Local ip: ', socket.gethostbyname(socket.gethostname()))
print()

while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn,addr = s.accept()
        with conn:
            print('[+] Connected to ', addr)
            while True:
                t = conn.recv(1024)
                if not t:
                    break
                data = t.decode()
    if data=='start':
        os.system("start pythonw Playmusic.py")
    elif data=='stop':
        os.system("taskkill /F /IM pythonw.exe")
    elif data=='exit':
        break
    else:
        print(data)
    time.sleep(0.2)
