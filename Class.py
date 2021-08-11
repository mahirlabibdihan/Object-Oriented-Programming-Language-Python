class Animal:
	def __init__(self,height,weight):
		self.height=height
		self.weight=weight
	def details(self):
		print("Height : "+str(self.height)+"  Weight : "+str(self.weight))

# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.
class Dog:
	pass
Tom = Animal(10,20)
print(type(Tom))
print(Tom.height)
Tom.details()
del Tom.height
# print(Tom.height) # Error
del Tom