#tmrine2,number of digits 
n=int(input("please enter a number: "))
i=1
sum=0

while n >= 10:
    sum=sum+(n % 10)
    n=n//10
    i=i+1

sum=sum+n
print("your number has ", i, "digits and your number is positive")
print("sum is ", sum)
print('average is', sum/i )