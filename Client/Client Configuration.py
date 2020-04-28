import os
import sys

def getServerIp():
    global serverIp
    serverIp = input("Server ip address: ")
    with open('client.conf', 'wt') as f:
        f.write(serverIp)
    print('serverIp <== ' + serverIp)
    i = input("Press Enter to exit...")
    
if not os.path.exists("client.conf"):
    getServerIp()
    sys.exit()
else:
    with open('client.conf', 'rt') as f:
        serverIp = f.read()

print("serverIp: " + serverIp)

while True:
    c = input("Do you want to change? [y/N] (default N): ")
    if c=='' or c=='N' or c=='n':
        sys.exit()
    elif c=='y' or c=='Y':
        getServerIp()
        sys.exit()
    else:
        continue
