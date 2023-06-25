import csv
PATH_TO_FILE = "D:/5.Git/PythonForEveryone/ex/genetic_code.csv"
infile=open(PATH_TO_FILE,"r")
csvreader=csv.reader(infile)
dict={}
temp=[]
out=""
indexStart=0

for line in csvreader:
    line[1]=line[1].strip("\"")
    temp=line[1].split(",")
    for i in range (len (temp)):
        temp[i]=temp[i].strip()
    dict[line[0]]=temp
    # print(line)

user=input("dna= ")

def findStart(ini,user,dict):
    for i in range(ini,len(user)):
        if user[i:i+3] in dict['start']:
            indexStart=i
            break
        else:
            indexStart=len(user)
    return indexStart

indexStart=findStart(0,user,dict)

for i in range(indexStart,len(user),3):
    print(user[i:i+3])
    for key in dict:
        if user[i:i+3] in dict[key]:
            if key=="stop":
                break
            elif key!="start":
                out=out+key
        else:
            indexStart=findStart(i,user,dict)

print(out)