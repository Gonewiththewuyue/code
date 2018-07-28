from sys import argv
script,textfile=argv
text=open(textfile,'r')
s=text.read()
print s
textfile1=raw_input("writefile name:")
text2=open(textfile1,'a+')
text2.write(s)
text2.seek(0)
s1=text2.read()
print s1
