from sys import argv
script,textfile=argv
text=open(textfile,'a')
line1="1111111111."
line2="222222222."
line3="333333333."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
