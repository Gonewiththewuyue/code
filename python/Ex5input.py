print "Ex5"
import numpy as np
r=6378
p=np.pi
s=4*np.pi*r**2
print "code:\n\t*radiu=\t%d\n\t*pi=\t%f\n\t*surface area=\t%f" %(r,p,s)
print
print "what is your name?"
name=raw_input()
print "how old are you?"
age=raw_input()
print "my name is %s and I am %s years old." %(name,age)
print 
name=raw_input("what is your name?")
age=raw_input("how old are you?")
print "my name is %s and I am %s years old." %(name,age)
