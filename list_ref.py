A=['T121','A551','Q156','T123']
B=[]
C=[]
i=0

while i< len(A):
    if 'T' in A[i]:
        A.pop(i)
    else:
        i=i+1

print(A)
        




