n=int(input( 'n = '))
i=0
s=0


while n != "":
    n=float(n)
    s=s+n
    i=i+1
    n=(input( 'n = '))

print(f'average is {s/i}')
