from mymodules import readIndex
from mymodules import BookIndex
from mymodules import printIndex


path="index.txt"
items=readIndex(path)
Dict=BookIndex(items)
printIndex(Dict)