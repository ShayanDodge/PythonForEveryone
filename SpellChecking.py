list=["Shayan","Book"]
user=input("word=")

uset=set(user.lower())
for i in range(len(list)):
    S=set(list[i].lower())
    print(S.difference(uset))
