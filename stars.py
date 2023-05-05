for i in range(4): 
    for j1 in range(4-i):
        print(" ",end='')
    for j2 in range(i+1):
        print("*",end='')
    for j3 in range(i):
        print("*",end='')
    print()
for i in range(4): 
    for j1 in range(i+1):
        print(" ",end='')
    for j2 in range(4-i):
        print("*",end='')
    for j3 in range(3-i):
        print('*',end='')
    print()

for i in range(5): 
    for j in range(5):
        if i%2==0 or j%2==0:
            print("$",end='')
        else:
            print(' ',end='')
    print()
