infile=open("music.txt",'r')
item=[]
list=[]
Set1=set()
Set2=set()
for line in infile:
    line=line.strip()
    item=line.split(";")
    for i in range(len(item)):
        item[i]=item[i].strip()
    list.append(item)
print(list)
user1=input("name=")
user2=input("first genre=")
user3=input("second genre=")

for i in range(len(list)):
    if user2 in list[i]:
        Set1.add(list[i][0])
    if user3 in list[i]:
        Set2.add(list[i][0])

for chr in sorted(Set1):
    print(chr)

for chr in sorted(Set2.difference(Set1)):
    print(chr)