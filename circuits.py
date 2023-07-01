number=input("the number of circuits = ")
time=input("max preparation time= ")

infile1=open("material.txt")
infile2=open("distributors.txt")
list=[]
mat=[]
store=[]
flg_time=0
flg_found=0

for lines in infile1:
    items=lines.split(",")
    for i in range(len(items)):
        items[i]=items[i].strip()
    mat.append(items)

for line in infile2:
    item=line.split(",")
    for i in range(len(item)):
        item[i]=item[i].strip()
    store.append(item)

for i in range(len(mat)):
    for ii in range(len(store)):
        if mat[i][0]==store[ii][1] and mat[i][1]==store[ii][4]:
            list.append(store[ii])
    for j in range(len(list)):
        if int(list[j][5])>=int(number)*int(mat[i][2]):
            flg_time=1
            if int(list[j][3])<=int(time):
                print(list[j])
                flg_found=1
                break
    if flg_time!=1 and flg_found!=1:
        print(mat[i],"not found")
    elif flg_time==1 and flg_found==0:
        print(mat[i],"more time need")
    flg_time=0
    flg_found=0
    list=[]