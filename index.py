


class Person:
	"""
	Declaring a function
	"""
	def __init__(self, name, age):
		self.name = name
		self.age = age

		"""
		displaying user inputs in a preferable form.
		"""
	def myFunc(self):
		print("Hello " + " " + self.name)
		print("You are " + " " + str(self.age) + " " + "old!")
		print("Welcome to the family!");


"""
taking user input names and Age
"""
names = input("Enter Your name:  ")
Age = int(input("Enter Your age: "))


"""
assigning user inputs in the class
"""
final = Person(names, Age)

"""
Testing the function if it's true then the results should be printed!
"""

def testFunc():
		assert Person(
			names == names,
			Age == Age,

		)
		
"""
calling the function testFunc()
"""
testFunc()


"""
calling the function myFunc()
"""
final.myFunc()

