def main():
    numbers=readnum()
    numbers=multiply(numbers,10)
    printreverse(numbers)
    
def readnum():
    print('pleaes input number: ')
    num=[]
    flg=True
    while flg:
        value=input('')
        if value=='Q':
            break
        value=float(value)
        num.append(value)
    return num   
    
def multiply(value,factor):
    for i in range(len(value)):
        value[i]=factor*value[i]
    return value
value=[i for i in range(100000)]       

def printreverse(numbers):
    i=len(numbers)-1
    while i>=0:
        print(numbers[i])
        i=i-1

main()