list=["1","2","3"]
list2=[]
user=input('=')
counter=0
list_new=[]
flg=0
while user !="":
    for j in list:
        if user==j:
            flg=1
    if flg==1:
        list2.append(user)
    else:
        print("not found")
    flg=0
    user=(input('='))

Set=set(list)

for item in Set:
    for j in list2:
        if item==j:
            counter=counter+1
    list_new.append([item,counter])
    counter=0

print(list_new)

for i in range(len(list_new)):
    if list_new[i][1]==0:
        print(list_new[i][0],"not found")
    else:
        print(list_new[i][0],list_new[i][1])