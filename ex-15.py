#-*- coding:utf-8 -*-
from sys import argv

script,file=argv

txt=open(file)

print "Here is the file %s"%file
print txt.read()

print "Type the file again:"
file_again=raw_input(">>>")

txt_again=open(file_again)

print txt_again.read()
#---------------------------------------#麻烦版复制内容
# print "Type the file:"
# file=raw_input(">>>")
# file1=open(file)
# data=file1.read()
# file2=raw_input("Type the new file:\n>>>")
# file3=open(file2,'w')
# file3.write(data)

# print "OK"

# file.close()
# file2.close()
#---------------------------------------#简化版复制内容
# print "Type the file:"
# file=raw_input(">>>")
# data=open(file).read()
# file2=raw_input("Type the new file:\n>>>")
# open(file2,'w').write(data)

# print "OK"


