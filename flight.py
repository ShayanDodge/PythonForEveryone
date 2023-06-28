infile = open("flightsdet.txt","r")
Table=[]
for line in infile:
    line = line.rstrip()
    line = line.strip(":.,!@#$")
    item = line.split(",")
    Table.append(item)

# print(Table)

city1 = input("from(Capital letters only)=")
city2 = input("ToCapital letters only=")


for i in range(len(Table)):
    if city1 == Table[i][2] and city2 == Table[i][4]:
        print(Table[i][0],Table[i][1],Table[i][2],Table[i][3],Table[i][4])
    else:
        for j in range (len(Table)):
            if Table[i][2] == city1 and Table[j][4] == city2:
                if Table[i][4] == Table[j][2]:
                    time1 = Table[i][3].split(":")
                    time2 = Table[j][1].split(":")
                    time11 = (int(time1[0])*60)+int(time1[1])
                    time22 = (int(time2[0])*60)+int(time2[1])
                    timedifference = time22 - time11
                    if timedifference<0:
                        timedifference=timedifference+1440
                    if abs(timedifference)<=300000000000:
                        print(Table[i][0],Table[i][1],Table[i][2],Table[i][3],Table[i][4])
                        print(Table[j][0],Table[j][1],Table[j][2],Table[j][3],Table[j][4])
                        print(timedifference)
                        print("------------------------------------")
