#usr/bin/python


import math
import random
import time 
def distance(x,y):
    return math.sqrt(x**2+y**2)
def main():
    NumofDots = input("请输入点的数量：") or 2**11
    DotsInCyc = 0
    time.clock()
    for i in range(int(NumofDots)):
        x = random.random()
        y = random.random()
        if distance(x,y) <= 1.0:
            DotsInCyc = DotsInCyc + 1
    pi = 4*(DotsInCyc/NumofDots)
    print("pi = %s" % pi)
    print("程序的运行时间是：%-5.5ss" % time.clock())

main()

    

