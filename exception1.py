try:
    path=input("please enter the path=")
    infile=open(path,"r")
except IOError:
    print("IOError")
except FileNotFoundError:
    print("FileNotFoundError")
else:
    infile.close()
