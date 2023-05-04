initialBalance=float(input( ' Initial Balance= '))
rate=float(input( ' rate= '))
numYears=int(input( ' years= '))
balance=initialBalance

print('years Balance')
print(15*'_')


for i in range(1,numYears+1):
    balance=balance+(balance*rate)
    print('%d  %10.2f' % (i, balance))

