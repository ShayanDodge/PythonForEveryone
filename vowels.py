name=input('whats your name?')
name=name.lower()
i=0
for char in name:
    if char in 'aeiou':
        i=i+1
print(i)