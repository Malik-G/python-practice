class Fighter: # this is a class called 'Fighter'
	
	def __init__(self, name): # this is a method (e.g. constructor method)
		self.name = name
		self.health = 100
		self.damage = 10
	
	def __str__(self): # this method is called if an object is the lone argument - see line 20
		return "{} : {}".format(self.name, self.health)

	def attack(self, opponent): # another method - called 'attack'
		opponent.health = opponent.health - self.damage
		print ("{} attacks {}!!".format(self.name, opponent.name))
		print ("{} has {} health remaining".format(opponent.name, opponent.health))

class Boxer(Fighter): # 'Boxer' inherits 
	def heal(self):
		self.health += 10
		print ("{} powers up!!".format(self.name))

'''malik = Fighter("Malik") # an object named Malik
glass = Fighter("Glass") # an object named Glass
glass.attack(malik)'''

boxerMalik = Boxer("Boxer M") 
boxerGlass = Boxer("Boxer G")

boxerGlass.attack(boxerMalik)
boxerMalik.heal()
print(boxerMalik)












