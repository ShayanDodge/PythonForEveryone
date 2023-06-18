list=[1,2,5,10,1,9,4]
list2=[1,1,1,1,2,2,2,2,2]
result=[]
Set=set(list)
i=0
for char in Set:
    for j in list2:
        if j==char:
            i=i+1
    result.append([char,i])
    i=0

for i in range(len(result)):
    if result[i][1]==0:
        print(result[i][0],"not found")
    else:
        print(result[i][0],"found",result[i][1])