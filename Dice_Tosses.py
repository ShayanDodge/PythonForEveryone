from random import randint
i=0

while True:
    i=i+1
    A1=randint(1,6)
    A2=randint(1,6)
    if A1==6 and A2==6:
        break
    print(A1,A2)

if i%2==0:
    print('K')
else:
    print('M')