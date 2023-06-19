name=["alex","fred","mary","sarah"]
number=[222,111,333,444]
contacts={}
for i in range(len(name)):
    contacts[name[i]]=number[i]

for (key,value) in contacts.items():
    print("%10s %10s"%(key,value))