import random

class Player(object):

	def __init__(self, name):
		self.name      = name
		self.health    = 10
		self.inventory = ["Medkit", "Grenade"]
		self.to_hit    = 50
		self.be_hit    = 25 
		self.defend    = False
		self.cooldown  = 0
		self.use_super = False

	def add_inventory(self, item):
		self.inventory.append(item)
		
	def list_inventory(self):
		print "You're currently carrying %d items." % len(self.inventory)
		for item in self.inventory:
			print "\t %s" % item.title()
		
	def attack(self, enemy):
		hit_chance = random.randint(1, 100)
		if hit_chance >= 50:
			print "Hit!"
			enemy.health -= 1
		else:
			print "Miss!" 

	def miss(self):
		print "You've missed ... everything!"

	def hit(self):
		to_hit = random.randint(1, 100)
		if to_hit <= self.to_hit:
			return True
		else:
			return False

	def super(self, evil):
		if self.cooldown <= 0:
			print "{0} has used their super!".format(self.name)
			self.use_super = True
			self.cooldown = 5
			for enemy in evil:
				enemy.health -= 2
		else:
			print "{0}, your super fizzles and makes you look stupid.".format(self.name)

	def defend(self):
		print "{0} shouts at the enemy, taunting them!".format(self.name)
		self.defend = True

	def cooldown_tracker(self):
		if self.cooldown != 0:
			self.cooldown -= 1
			
		if self.use_super and self.cooldown != 0:
			print "{0}, {1} more rounds until your super is ready.".format(self.name, self.cooldown)			
		elif self.cooldown == 0:
			print "{0}, your super is ready.".format(self.name)
			self.use_super = False
			self.cooldown = 5

