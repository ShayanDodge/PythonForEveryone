string=input (' string= ')
flag=len(name)==13
i=0

while flag and i<len(string):
    if i==0:
        flag=string[i]=='('
    elif i==4:
        flag=string[i]==')'
    elif i==8:
        flag=string[i]=='_'
    else:
        flag=string[i].isdigit()
    i=i+1

if flag:
    print(' the string is valid')
else:
    print(' the string is not valid')


