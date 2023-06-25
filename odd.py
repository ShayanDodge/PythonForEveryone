def munodi(seq):
    sit=0
    if len(seq) == 1:
        sit=0
    else:
        for i in range(len(seq)-1):
           j=i+1
           if int(seq[i])%2==0:
               if float(seq[i])/2==float(seq[i+1]):
                  i=i+1
               else:
                  sit=1
                  break
           elif float(seq[i+1])==float(seq[i])*3+1:
                 i=i+1
           elif float(seq[i+1])!=float(seq[i])*3+1:
                 sit=1
                 break

    return sit


infile=open("monudi.txt","r")
line=infile.readline()
list=[]
while line!="":
    items=line.split()
    list.append(items)
    line = infile.readline()
for i in range(len(list)):
    munodi(list[i])
    if munodi(list[i])==0:
        print(list[i],"munodi")
    else:
        print(list[i],"not monodi")