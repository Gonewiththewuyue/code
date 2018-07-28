from sys import argv
script,textfile=argv
text=open(textfile,'w')
line1="There is Zhichao Liang next to me.."
line2="He is very smart.."
line3="He said he was xiaoming."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
