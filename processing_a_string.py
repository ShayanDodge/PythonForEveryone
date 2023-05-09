string=input('string=')
string_m=""

for char in string:
    if char!="_" and char!=" ":
        string_m=string_m+char

print(string_m)