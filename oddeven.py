infile=open("monudi.txt","r")
line=infile.readline()
list=[]
while line!="":
    items=line.split()
    list.append(items)
    line = infile.readline()

for i in range(len(list)):

    sit=0
    if len(list[i]) == 1:
        sit=0
    else:
        for k in range(len(list[i])-1):
           if int(list[i][k])%2==0:
               if float(list[i][k])/2==float(list[i][k+1]):
                  k=k+1
               else:
                  sit=1
                  break
           elif float(list[i][k+1])==float(list[i][k])*3+1:
                 k=k+1
           elif float(list[i][k+1])!=float(list[i][k])*3+1:
                 sit=1
                 break

    if sit==0:
        print(list[i],"munodi")
    else:
        print(list[i],"not monodi")