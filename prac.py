class Animal:
	def __init__(self, species, name, age):
		self.species = species
		self.name = name
		self.age = age
	def birthday(self):
		print("Happy birthday, %s" % self.name)
		self.age += 1


bennett = Animal("Human", "Bennett", 20)
print(bennett.age)
bennett.birthday()
print(bennett.age)