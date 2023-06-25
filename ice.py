infile=open("ice.txt","r")
line=infile.readline()
line=line.strip()
items=[]
dict={}
while line:
    item=line.split(":")
    items.append(item)
    line=infile.readline()
    line=line.strip()

for j in range(len(items[0])):
    for i in range(len(items)):
        print("%7s"%items[i][j],end="")
    print()
