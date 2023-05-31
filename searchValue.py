value=[i for i in range(1,1001)]
searchedValue=100
pos=0
flg=False

for i in range(len(value)):
    if value[i]>searchedValue:
        pos=i
        flg=True
        print(pos)
        break
    
if flg==False:
    print('not found')