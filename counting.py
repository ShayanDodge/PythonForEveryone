value=[i for i in range(1,1001)]
result=[]
result2=[]
j=0
val=value[:]
for i in range(len(value)):
    if value[i]>100:
        result.append(value[i])
        val.remove(value[i])
        j=j+1
# print(result)
print(val)
print(j)

