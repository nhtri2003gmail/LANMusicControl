import os
import sys

def getMusicPath():
    global musicPath
    musicPath = input("Path to Music Folder: ")
    with open('server.conf', 'wt') as f:
        f.write(musicPath)
    print("Music_Folder <== " + musicPath)
    i = input("Press Enter to exit...")
    
if not os.path.exists("server.conf"):
    getMusicPath()
    sys.exit()
else:
    with open('server.conf', 'rt') as f:
        musicPath = f.read()

print("Music_Folder: \"" + musicPath + '\"')

while True:
    c = input("Do you want to change? [y/N] (default N): ")
    if c=='' or c=='N' or c=='n':
        sys.exit()
    elif c=='y' or c=='Y':
        getMusicPath()
        sys.exit()
    else:
        continue
