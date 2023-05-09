name=input(' name= ')
i=len(name)-1
while True:
    if name[i].isupper():
        print(i)
        break
    i=i-1