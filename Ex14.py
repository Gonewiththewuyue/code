import numpy as np
def circumference(r):
    return 2*np.pi*r
from sys import argv
script,r=argv
print "the script is called:",script
print "the redius is:",r
cx=2*np.pi*float(r)
print "the circumference is:",cx
r1=6378
r2=3396
d1=abs(float(r)-r1)
d2=abs(float(r)-r2)
if d1<d2:
    print "near Earth"
elif d1>d2:
    print "near Mars"
else:
    print "the same"
