list=[["cont","gold","silver","bronze"],["usa",1,0,2],["Italy",1,1,4]]
temp=0
for i in range(len(list)):
    # if i==len(list)+1:
    #     list.append()
    for j in range(len(list[i])):
        print("%10s"%list[i][j],end=" ")
        if i>0 and j>0:
            temp=temp+list[i][j]
    if i==0:
        list[i].append("total")
    else:
        list[i].append(temp)
    print("%10s"%list[i][j+1],end=" ")
    print()
    
for j in range(len(list[0])):
    for i in range(len(list)):
        if i>0 and j>0:
            temp=list[i][j]+temp
    if j==0:
        print("%10s"%"total",end=" ")
    else:
        print("%10s"%temp,end=" ")
    temp=0
