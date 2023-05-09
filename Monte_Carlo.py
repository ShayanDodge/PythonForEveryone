from random import random
tries=100000000
hit=0
for i in range(tries):
    r=random()
    x=-1+2*r
    r=random()
    y=-1+2*r
    if x*x+y*y<=1:
        hit=hit+1

PiNumber=4*hit/tries
print(PiNumber)