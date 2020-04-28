import os
import sys

def PartGate():
    os.system('ifconfig | grep 192 > ifconfig.txt')
    with open("ifconfig.txt", 'rt') as f:
        ip = f.read()
    os.system('rm ifconfig.txt')
    t = ip.split(' ') ## Wrong at this place
    
    defWay = str(t[len(t)-1])
    
    partNum = defWay.split('.')
    finNum = str(partNum[0]) + '.' + str(partNum[1]) + '.' + str(partNum[2]) + '.'
    return finNum
