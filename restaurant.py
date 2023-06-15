infile1=open('text.txt','r')
infile2=open('text2.txt','r')
outfile=open('text3.txt','w')

temp=[]
menu=[]
number=[]
recit=[]
price=0
total=0
tax=0

line1=infile1.readline()
line2=infile2.readline()

while line1:
    temp=line1.split(':')
    for i in range(len(temp)):
        temp[i]=temp[i].strip()
    menu.append(temp)
    line1=infile1.readline()

while line2:
    temp=line2.split(':')
    for i in range(len(temp)):
        temp[i]=temp[i].strip()
    number.append(temp)
    line2=infile2.readline()

k=0

for i in range(len(menu)):
    for j in range(len(number)):
        if menu[i][0]==number[j][0]:
            recit.append(menu[i])
            price=float(menu[i][2])*float(number[j][1])
            recit[k][2]=price
            total=price+total
            k=k+1

tax=total+total*0.2

print("%-10s" %"N",end="",file=outfile)
print("%-10s" %"F",end="",file=outfile)
print("%-10s" %"P",file=outfile)
print(25*"-",file=outfile)
for i in range(len(recit)):
    print("%-10s" %recit[i][0],end="",file=outfile)
    print("%-10s" %recit[i][1],end="",file=outfile)
    print("%-10d" %recit[i][2],file=outfile)
print("total",':',total,file=outfile)
print("tax",'  :',tax,file=outfile)

infile1.close()
infile2.close()
outfile.close()



