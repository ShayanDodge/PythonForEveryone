# The program checks if a substring is present in a given string using
# the "in" operator
name=input('name=')
substring=input('sub=')

if substring in name:
    name=name.replace(substring,'')
    print (name)
else:
    print(name)