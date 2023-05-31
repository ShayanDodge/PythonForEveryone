values=[]
print('please insert a value, Q to Quit:')
temp=input('')
while temp.upper() != 'Q':
    values.append(float(temp))
    temp=input('')

largest=values[0]
for i in range(len(values)):
    if values[i]>largest:
        largest=values[i]

for i in values:
    if i==largest:
        print('>>',end='')
    print(i,end='')
    if i==largest:
        print('<<',end='')
    print('')

