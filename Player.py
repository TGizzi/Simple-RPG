import random
from Item import ItemList, Item

class Player(object):

	def __init__(self, name):
		self.name      = name
		self.health    = 10
		self.inventory = [ItemList.Medkit(), ItemList.Grenade(2)]
		self.to_hit    = 50
		self.be_hit    = 25 
		self.defend    = False
		self.cooldown  = 5
		self.use_super = False

	def add_inventory(self, item):
		self.inventory.append(item)
		
	def list_inventory(self):
		print "You're currently carrying %d items." % len(self.inventory)
		for item in self.inventory:
			print "\t %s" % item.title()
		
	def hit(self):
		to_hit = random.randint(1, 100)
		if to_hit <= self.to_hit:
			return True
		else:
			return False

	def cooldown_tracker(self):
		if self.use_super and self.cooldown != 0:
			self.cooldown -= 1
			print "{0}, {1} more rounds 'til your super is ready.".format(self.name, self.cooldown)
		elif self.cooldown == 0:
			print "{0}, your super is ready.".format(self.name)
			self.use_super = False
			self.cooldown = 5
