infile = open ("actions.txt",'r')
magic_box=[list() for i in range(42)]
items=[]
flg=1
indx=0
for line in infile:
    try:
        items=line.split()
        if items[0]!="Bob" and items[0]!="Carl":
            raise ValueError("ffd")
    except(ValueError):
        print("unknown")
        break
    indx=indx+1
    flg=1
    for i in range(len(magic_box)):
        if items[1]=="gives":
            if magic_box[i]==[]:
                magic_box[i].append(items[3])
                flg=0
                break
            elif items[3] in magic_box[i]:
                magic_box[i].append(items[3])
                flg=0
                break
        else:
            if items[3] in magic_box:
                magic_box[i].pop(0)
                flg=0
                break
    if flg==1:
        print("cannot %5s from %5s" %(items[1],items[0]))
        break
