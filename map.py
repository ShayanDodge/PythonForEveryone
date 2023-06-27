infile=open("map.txt")
list=[]
for line in infile:
    line=line.strip()
    list.append(line)

row=int(input("row="))
col=int(input("col="))
print(list[row][col])

if list[row][col]=="=":
    print("=")
else:
    while list[row][col]==list[row+1][col]:
        row=row+1
    up=row
    while list[row][col]==list[row-1][col]:
        row=row-1
    down=row
    while list[row][col]==list[row][col+1]:
        col=col+1
    right=col
    while list[row][col]==list[row][col-1]:
        col=col-1
    left=col

print(up-down+1)
print(right-left+1)