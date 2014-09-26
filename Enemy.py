import random

class Enemy(object):
	
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def hit(self, taunt):
		if taunt:
			hit_chance = 10
		else:
			hit_chance = 25
		enemy_hit_chance = random.randint(1, 100)
		if enemy_hit_chance <= hit_chance:
			return True
		else:
			return False

def get_enemy(number):

	active_enemies = []

	enemies = [{'name': 'Hipster', 'health': 5}, {'name': 'Youths', 'health': 5}, 
				{'name': 'Kittens', 'health': 5}, {'name': 'Feeble Youths', 'health': 3},
				{'name': 'Robots', 'health': 7}, {'name': 'Devin from Big Brother', 'health': 10}]

	for i in xrange(number):
		enemy = random.choice(enemies)
		active_enemies.append(Enemy(enemy['name'], enemy['health']))
	return active_enemies
