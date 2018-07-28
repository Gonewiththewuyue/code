from sys import argv
script,textfile=argv
text=open(textfile,'w')
line1="555555."
line2="H666666666666."
line3="H88888888888."
text.write(line1)
text.write("\n")
text.write(line2)
text.write("\n")
text.write(line3)
text.write("\n")
text.close()
