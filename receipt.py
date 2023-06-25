infile = open("receipt.txt","r")
outfile= open("receipt1.txt","w")
menu=[]
recieptmenu=[]
for line in infile:
    line=line.rstrip()
    line=line.strip(",.:!&*$? ")
    item=line.split()
    for i in range (len(item)):
        item[i]=item[i].strip()
        item[i]=item[i].strip(" ,!&^:$")
        # if i == item[2]:
        #     item[i]=float(item[i])
    menu.append(item)




for i in range(len(menu)):
    j=0
    while j<len(menu[i]):
        if menu[i][j]=="":
            menu[i].pop(j)
        else:
            j=j+1
menu_new=[]
temp=""
for i in range(len(menu)):
    for j in range(len(menu[i])):
        if menu[i][j][0].isdigit()==False:
            temp=temp+" "+menu[i][j]
    temp=temp.strip()
    temp_list=[menu[i][0],temp,menu[i][-1]]
    menu_new.append(temp_list)
    temp=""

userinput=input("wich number is your order? ")
count=[0]* (len(menu_new))
while userinput:
    for i in range (len(menu_new)):
        if userinput == menu_new[i][0]:
            count[i]=count[i]+1
    userinput=input("what else: ")

price = [0]*(len(menu_new))
for i in range (len(menu_new)):
    price[i]=int(count[i])*float(menu_new[i][2])
    recieptmenu.append(price[i])
    if price[i]!=0:
        print("%-10s %-50s %-10s"%(menu_new[i][0],menu_new[i][1],price[i]),file=outfile)