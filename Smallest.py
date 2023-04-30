n=int(input(' n = '))
smallest=n

while True:
    if n<smallest:
        smallest=n
    n=int(input(' n = '))
    if n<0:
        break

print('The smallest number is %f'%smallest)