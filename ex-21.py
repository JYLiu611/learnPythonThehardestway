def add(a,b):
	print "%d + %d "%(a,b)
	return a+b
	
def subtract(a,b):
	print "%d - %d "%(a,b)
	return a-b
	
def multiply(a,b):
	print "%d * %d "%(a,b)
	return a*b
	
def divide(a,b):
	print "%d / %d "%(a,b)
	return a/b
	
age=add(30,5)
height=subtract(195,3)
weight=multiply(96.5,2)
iq=divide(200,2)
print """
age is %d
height is %d
weight is %d
iq is %d
 """%(age,height,weight,iq)
 
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ",what, "Can you do it by hand?"
 
