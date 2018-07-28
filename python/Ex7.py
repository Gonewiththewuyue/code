from sys import argv
import numpy as np
script,r=argv
print "the script is called:",script
print "the redius is:",r
print "the circumference is:",2*np.pi*float(r)
print 
print "use in_put"
name=raw_input("Your Earth's name:")
r=float(raw_input("radius:"))
c=2*np.pi*r
print "circumference is %f" %c
