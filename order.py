infile=open('menu.txt','r')
outfile=open("outt.txt",'w')
menu=[]
for line in infile:
    line=line.strip()
    items=line.split()
    for i in range(len(items)):
        items[i]=items[i].strip()
        items[i]=items[i].strip(".:$")
        if i==len(items)-1:
            items[i]=float(items[i])
    items.remove("")
    menu.append(items)

count=(len(menu))*[0]
user=input("=")
while user:
    for i in range(len(menu)):
        if user==menu[i][0]:
            count[i]=count[i]+1
    user=input("=")
print(count)

price=(len(menu))*[0]
for i in range(len(menu)):
    price[i]=count[i]*menu[i][2]

for i in range(len(menu)):
    print("%5s. %5s : %5s * %1s = %5s"%(menu[i][0],menu[i][1],menu[i][2],count[i],price[i]),file=outfile)