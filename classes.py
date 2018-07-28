class goodman(object):
    def __init__(self):
        self.glasses=True
        self.cancook=True
    def character(self):
        print "smart and handsome"

class organism(object):
    def __init__(self):
        self.eat=True
class animals(organism):
    def __init__(self):
        super(animals,self).__init__()
        self.moving=True
        self.breath=True
class vertebrate(animals):
    def __init__(self):
        super(vertebrate,self).__init__()
        self.spnie=True
class mammal(vertebrate):
    def __init__(self):
        super(mammal,self).__init__()
        self.hand=True
        self.egg=False
class dog(mammal):
    def __inti__(self):
        super(dog,self).__init__()
        self.milk=True
    def character(self):
        print "wangwangwang"
        print "small is good"
print 
class people(object):
    def implicit(self):
        print "the old people want to go back young"
class child(people):
    pass
    
class student(object):
    def override(self):
        print "Not everyone has a good character"
    def altered(self):
        print "everyone can be good"
class tj(student):
    def override(self):
        print "but tj student has a good character"
    def altered(self):
        print "everyone tj student is good"
        super(tj,self).altered()

class man(object):
    def character(self):
        print "chengwen zhuangzhong "
class boy(object):
    def __init__(self):
        self.man=man()
    def character(self):
        self.man.character()
    


