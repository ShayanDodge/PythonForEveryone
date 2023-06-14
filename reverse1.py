temp=0
list=[]
while temp!='':
    temp=input("please=")
    if temp=="":
        break
    list.append(int(temp))
list2=len(list)*[0]
for i in range(len(list)):
    list2[i]=list[len(list)-i-1]

print(list2)