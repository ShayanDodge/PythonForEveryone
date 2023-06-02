def main():
    numbers=countInput()
    printnum(numbers)
    
def countInput():
    counter=6*[0]
    while True:
        value=input('')
        if value=='Q':
            break
        value=int(value)
        if (value)>=1 and (value)<=6:
            counter[(value)-1]=counter[(value)-1]+1
        else:
            break
    return counter
    
def printnum(counter):
    for i in range(0,len(counter)):
        print(i+1,counter[i])
main()