infile=open("text1.txt")
list=[]
for line in infile:
    item=line.split()
    for char in item:
        list.append(char)
word1=input("word1=")
word2=input("word2=")
# print(list)

flg_ini=0
flg_last=0
for i in range(len(list)):
    if word1==list[i]:
        ini=i
        flg_ini=1
        break
for i in range(len(list)):
    if word2==list[i]:
        last=i
        flg_last=1
        break

if flg_last==1 and flg_ini==1:
    print(last-ini-1)
else:
    print("not found")
