infile=open('text.txt','r')
outfile=open('text3.txt','w')
words=[]
word=infile.read(1)
words.append(word)
while word:
    word=infile.read(1)
    words.append(word)
# print(words)
temp=words[0]
count=0
count_list=[]
i=0
j=0
while words:
    temp=words[0]
    while i<len(words):
       if temp==words[i]:
           count=count+1
           words.pop(i)
       else:
            i=i+1
    count_list.append([temp,count])
    i=0
    count=0
print('C',end="  ",file=outfile)
print('C',end="  ",file=outfile)
print('',file=outfile)
for i in range(len(count_list)-1):
    for j in range(len(count_list[i])):
        print(count_list[i][j],end="  ",file=outfile)
    print("",file=outfile)

infile.close()
outfile.close()
