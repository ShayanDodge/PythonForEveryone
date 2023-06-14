list=[10,15,20,4,8,6,0]
max=list[0]
index_max=0
for i in range(len(list)):
    if list[i]>max:
        max=list[i]
        index_max=i
for i in range(len(list)):
    if i==index_max:
        print(list[i],"*")
    else:
        print(list[i])

