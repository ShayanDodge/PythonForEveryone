from random import random

def Pi_MC(decimal):
    tries = 0
    hit = 0
    piNumber=0
    while (piNumber-3)<decimal:
        tries=tries+1
        r = random()
        x = -1+2*r
        r = random()
        y = -1+2*r
        if x*x+y*y <= 1:
            hit = hit+1  
    piNumber = 4*hit/tries
    print(piNumber)
    return piNumber

p=Pi_MC(0.1)