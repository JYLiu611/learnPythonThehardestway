print "TRY "
print 'You\'d need to know \'bout escapes with \\ that do \n newlin'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------\n",poem,"\n--------------"

def cal(r):
	d=2*float(r);
	from math import pi
	s=pi*float(r)*float(r)
	l=2*pi*float(r)
	return d,s,l

radium=raw_input("r=")
d,s,l=cal(radium)
print "With r: %s" %radium
print "We'd have d = %d s = %.2f,l = %.2f." % (d,s,l)

print "IF r = half r \n then"
print "We'd have d = %d \n	s = %.2f \n l = %.2f." % cal(0.5*float(radium))