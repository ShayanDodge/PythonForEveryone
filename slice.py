list=['a','b','c','d','e','f','g','p','a','b']
list_count=[]
list2=[]
i=0
j=0
temp=0
count=0
while list:
    temp=list[0]
    while j<len(list):
        if temp==list[j]:
            list.pop(j)
            count=count+1
        else:
            j=j+1
    list_count.append(count)
    list2.append(temp)
    count=0
    j=0
for ind in range(len(list2)):
    print(list2[ind],"  ",list_count[ind])




