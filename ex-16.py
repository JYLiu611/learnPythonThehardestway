#-*- coding:utf-8 -*-
from sys import argv
script,filename=argv

print "We are going to erase %s."%filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Open the file..."
file=open(filename,'r')
print "Now the words are:\n",file.read()
print "Truncating the file.  Goodbye!"

file.close()#读完关闭
file=open(filename,'w')
file.truncate()

print "Now I'm going to ask you for three lines."
line1=raw_input("line1:>>>")
line2=raw_input("line2:>>>")
line3=raw_input("line3:>>>")

print "I'm going to write these to the file."
file.write(line1+"\n"+line2+"\n"+line3+"\n")

print "And finally, we close it."
file.close()