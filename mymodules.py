def readIndex(path):
    items=[]
    infile=open(path,"r")
    line=infile.readline()
    line=line.rstrip()
    while line!="":
        item=line.split(":")
        items.append(item)
        line=infile.readline()
        line=line.rstrip()
    return items

def BookIndex(items):
    ref=set()
    value=set()
    Dict={}
    for i in range(len(items)):
        ref.add(items[i][0])
    for key in ref:
        for i in range(len(items)):
            if key == items[i][0]:
                value.add(items[i][1])
        Dict[key]=value
        value=set()
    return Dict

def printIndex(Dict):
    for key in sorted(Dict):
        print("%10s : %10s" %(key,Dict[key]))