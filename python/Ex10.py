import numpy as np
def circumference(r):
    return 2*np.pi*r

r1=6378
print "Earth's circumference:\t",circumference(r1)
r2=3396
print "Mars's circumference:\t",circumference(r2)
