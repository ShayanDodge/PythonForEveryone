import math
r=math.sqrt(2.0)
eps=0.0000001
if r*r<2.0+eps or r*r>2.0-eps:
    print('sqrt(2.0)*sqrt(2.0) is 2.0')
else:
    print('sqrt(2.0)*sqrt(2.0) is not 2.0')
    