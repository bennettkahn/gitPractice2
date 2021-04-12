class Animal:
	def __init__(self, species, name, age):
		self.species = species
		self.name = name
		self.age = age
	def birthday(self):
		print("Happy birthday, %s" % self.name)
		self.age += 1


bennett = Animal("Human", "Bennett", 20)
corinne = Animal("Human", "Corinne Fruge", 20)


print(bennett.age)
bennett.birthday()
print(bennett.age)
bennett.name = "Bennett Kahn"
print(bennett.name)
print(corinne.age)
corinne.birthday()
print(corinne.age)


print("YO I BE TESTING STUFF")
print("I be printing stuff in Bennett")
print("I be testing stuff in new")
print("I be testing stuff in new")


print("is this thing on")

