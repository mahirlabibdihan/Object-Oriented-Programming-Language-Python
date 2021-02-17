# Create a global variable outside of a function
x=10

def f1():
	print(x)
	# We can't change the value of global variable from function
	# x=5 # Error

# Create a global variable inside a function
def f2():
	# a=5 # definition before global declaration is invalid
	global a # Declaration
	# print(a) # Error - a is not defined
	a=5 # Definition
	print(a)

# Change the value of global variable from function
def f3():
	global x
	print(x)
	x=5
	print(x)

f1()
f2()
f3()