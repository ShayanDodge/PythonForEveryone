def sum(list):
    temp=0
    for i in range(len(list)):
        temp=list[i]+temp
    return temp

print(sum([1,2,3,45,5]))
