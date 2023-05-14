from random import randint

def main():
    result=makepass(8)
    print(result)
    
def makepass(length):
    password=''
    for i in range(length-2):
        password=password+rendom_char('abcdefghijklmnop')
    randomDigit=rendom_char('0123456789')
    password=insert_random(password,randomDigit)
    randomSym=rendom_char('!@#$%^&*()_+')
    password=insert_random(password,randomSym)
    return password

def rendom_char(char):
    n=len(char)
    i=randint(0,n-1)
    return char[i]

def insert_random(string,specialChar):
    n=len(string)
    i=randint(0,n)
    result=''
    for ind in range(i):
        result=result+string[ind]
    result=result + specialChar
    for ind in range(i,n):
        result=result+string[ind]
    return result
main()
    
    
        