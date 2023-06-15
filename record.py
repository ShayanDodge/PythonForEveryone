infile=open("text.txt",'r')
line=infile.readline()
line=line.rstrip()
cont=[]
pop=[]
loc=0
while line:
    i=0
    for char in line:
        if char.isdigit():
            loc=i
            break
        i=i+1
    cont.append(line[0:loc])
    pop.append(line[loc:])

    line=infile.readline()
    line=line.rstrip()
print(cont)
print(pop)