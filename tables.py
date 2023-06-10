table=[["country","gold","silver"],["canada",0,3],["italy",1,2]]

total=0
table[0].append("total")
for i in range(1,len(table)):
    for j in range(1,len(table[i])):
        total=table[i][j]+total
    table[i].append(total)
    total=0

total_list=['total']
total=0
for j in range(1,len(table[0])):
    for i in range(1,len(table)):
        total=table[i][j]+total
    total_list.append(total)
    total=0
table.append(total_list)

for i in range(len(table)):
    for j in range(len(table[i])):
        if (i==0) or (j==0):
            print( '%20s' %table[i][j],end=" ")
        else:
            print( '%20d' %table[i][j],end=" ")
    print()