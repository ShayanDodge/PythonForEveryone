def cube_volume(l):
    if l>0:
        return l**3
    else:
        return 'please change the number'
    
volume=cube_volume(int(input('l=')))
print(volume)