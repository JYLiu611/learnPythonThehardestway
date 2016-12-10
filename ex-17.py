# -*- coding: utf-8 -*-
from sys import argv
from os.path import exists

script,from_file,to_file=argv

print "Copy from %s to %s"%(from_file,to_file)
data=open(from_file).read()

print "This input is %d bytes long."%len(data)

print "Does this output file exist? %r"%exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()
open(to_file,'w').write(data)

print "Alright, all done."

open(from_file).close()
open(to_file).close()