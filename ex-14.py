from sys import argv
script,name=argv

prompt=">>>>  "
print "Hi %s,I`m the %s`s script."%(name,script)
print "I`d like to ask you a few questions."
print "Do you like me,%s?"%name
likes=raw_input(prompt)

print "Where do you live,%s?"%name
lives=raw_input(prompt)

print "What kind of computer do you have,%s?"%name
com=raw_input(prompt)

print'''
Alright, so you said %s about liking me.
You live in %s.  Not sure where that is.
And you have a %s computer.  Nice.
''' % (likes, lives, com)