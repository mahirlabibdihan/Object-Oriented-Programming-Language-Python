class Animal:
	def __init__(self,height,weight):
		self.height=height
		self.weight=weight
	def details(self):
		print("Height : "+str(self.height)+"  Weight : "+str(self.weight))

class Dog(Animal):
	def __init__(self,name,height,weight):
		# Animal.__init__(height,weight)
		super().__init__(height,weight)
		self.name=name
	def details(self):
		print("Name : "+self.name,end("  "))
		super().details()

