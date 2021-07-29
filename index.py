


class Person:
	
	def __init__(self, name, age):
		"""
	inputs:
		-user name
		-user age
	outputs
		-null
	"""
		self.name = name
		self.age = age

		
	def myFunc(self):
		"""
		inputs:
			-null
		ouputs:
			-user name
			-user age
		"""
		print("Hello " + " " + self.name)
		print("You are " + " " + str(self.age) + " " + "old!")
		print("Welcome to the family!");


names = input("Enter Your name:  ")
Age = int(input("Enter Your age: "))

"""
names = names,
Age = age
"""
final = Person(names, Age)
final.myFunc()

