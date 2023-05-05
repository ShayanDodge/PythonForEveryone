#tamrin3,table with while and for
n = 10
m =4
i=1
for ii in range(1,m+1):
    print("%s%-9d"%("x^",ii),end="")
print()
print(20*"* ")


while i<=n:
    for j in range(1,m+1):
        print("%-10d "%i**j,end="")

    print()
    i = i + 1
    print(20*"* ")