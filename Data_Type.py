# Built-in Data Types

# Text Type:		str
# Numeric Types:	int, float, complex
# Sequence Types:	list, tuple, range
# Mapping Type:		dict
# Set Types:		set, frozenset
# Boolean Type:		bool
# Binary Types:		bytes, bytearray, memoryview

x = "Hello World"								# str	
print(type(x))
x = 20											# int	
print(type(x))
x = 20.5										# float	
print(type(x))
x = 1j											# complex	
print(type(x))
x = ["apple", "banana", "cherry"]				# list	
print(type(x))
x = ("apple", "banana", "cherry")				# tuple	
print(type(x))
x = range(6)									# range	
print(type(x))
x = {"name" : "John", "age" : 36}				# dict	
print(type(x))
x = {"apple", "banana", "cherry"}				# set	
print(type(x))
x = frozenset({"apple", "banana", "cherry"})	# frozenset	
print(type(x))
x = True										# bool	
print(type(x))
x = b"Hello"									# bytes	
print(type(x))
x = bytearray(5)								# bytearray
print(type(x))	
x = memoryview(bytes(5))						# memoryview
print(type(x))