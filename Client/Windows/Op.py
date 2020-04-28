import os
import sys

def PartGate():
    os.system('ipconfig > ipconfig.txt')
    with open("ipconfig.txt", 'rt') as f:
        ip = f.read()
    os.system('del ipconfig.txt')
    t = ip.split('\n')
    defWay = str(t[len(t)-2])
    gateWay = defWay.split(':')
    num = str(gateWay[1])
    i=1
    newNum=''
    while i<len(num):
        newNum+=num[i]
        i+=1
    partNum = newNum.split('.')
    finNum = str(partNum[0]) + '.' + str(partNum[1]) + '.' + str(partNum[2]) + '.'
    return finNum
