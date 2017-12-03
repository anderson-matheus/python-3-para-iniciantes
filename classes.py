class Pessoa:

	def __init__(self, name):
		self.name = name

	def getName(self):
		return self.name

	def setName(self, name):
		self.name = name

person = Pessoa('Marcos')
print(person.getName())

person.setName('Anderson')
print(person.getName())
