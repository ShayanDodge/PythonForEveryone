# The program checks if a string starts or ends with a given substring
# using the "startswith" and "endswith" methods:
name=input('name=')
sub=input('sub=')
if sub in name:
    if name.startswith(sub):
        if name.endswith(sub):
            print('name starts and ends with',sub)
        else:
            print('name starts with',sub)
    elif name.endswith(sub):
        print('name ends with',sub)
    else:
        print('There is ',sub, 'in name')
else:
    print('There is not ',sub, 'in name')