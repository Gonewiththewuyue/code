def print_none():
    print "Hello world."
def print_one(arg):
    print "I like %r." %arg
def print_two(arg1,arg2):
    print "I like %r and %r." %(arg1,arg2)
def add(a,b):
    return a+b

print_none()
print_one("apple")
print_two("apple","banana")
A=20
B=30
total=add(A,B)
print "Total is %d" %total

