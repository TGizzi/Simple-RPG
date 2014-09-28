import random
import code
from Item import Item

class Battle(object):

	def combat_check(self, evil):
		in_combat = False
		for enemy in evil:
			if enemy.health > 0:
				in_combat = True
				break
		return in_combat

	def fight(self, good, evil):
		in_combat = True
		while in_combat:
			for player in good:
				hasMedkit = False
				hasGrenade = False
				
				if not self.combat_check(evil):
					break
				if player.health > 0:
					print "+" * 20
					print "{0}, you're up!".format(player.name)
					print "+" * 20

					for number, friend in enumerate(good, start = 1):
						print "{0} has {1} health left.".format(friend.name, friend.health)
						print "+" * 20
					for number, enemy in enumerate(evil, start = 1):
						print "{0} ({2}) has {1} health left.".format(enemy.name, enemy.health, number)
						print "+" * 20

					choices = "Choose "
					for number, enemy in enumerate(evil, start = 1):
						if enemy.health > 0:
							choices += "attack enemy {0}, ".format(number)
					choices += "'defend', 'super'" 

					itemChoices = ""
					for item in player.inventory:
						if item.name == "Medkit":
							itemChoices += ", 'medkit <name>'"
							hasMedkit = True

						if item.name == "Grenade":
							itemChoices += ", 'grenade'"
							hasGrenade = True

					choices += itemChoices + ":"
					print choices

					cmd = raw_input(">> ")
					for number, enemy in enumerate(evil, start = 1):
						if cmd.lower() == "attack enemy {0}".format(number) and enemy.health > 0:
							hit_chance = random.randint(1, 100)
							if hit_chance >= 50:
								print "Hit!"
								enemy.health -= 1
							else:
								print "Miss!" 
						elif cmd.lower() == "attack enemy {0}".format(number):
							print "The confusion of battle causes you to miss an alive target!"

					if cmd.lower() == "defend":
						print "{0} shouts at the enemy, taunting them!".format(player.name)
						player.defend = True
					elif cmd.lower() == "super":
						print "{0} SOMETHING COOL ABOUT USING A SUPER".format(player.name)
						player.use_super = True
						if player.cooldown <= 0:
							for enemy in evil:
								enemy.health -= 1
						else:
							print "{0}, you can't use your super yet".format(player.name)
					elif cmd.lower() == "grenade" and hasGrenade:
						for item in player.inventory:
							if item.name == "Grenade":
								item.count -= 1
								print "{0} tosses a grenade at the enemies.".format(player.name)
								if item.count <= 0:
									player.inventory.remove(item)
								break
						for enemy in evil:
							if enemy.health > 0:
								enemy.health -= 1
					else:
						for friend in good:
							if cmd.lower() == "medkit {0}".format(friend.name.lower()) and friend.health > 0:
								if friend == player:
									print "{0} uses a medkit to heal themself"
								else:
									print "{0} uses a medkit to heal {1}".format(player.name, friend.name)
								friend.health += 3
								friend.health = min(10, friend.health)
								for item in player.inventory:
									if item.name == "Medkit":
										item.count -= 1
										if item.count <= 0:
											player.inventory.remove(item)
										break
								break

			for number, enemy in enumerate(evil, start = 1):
				if not self.combat_check(good):
					print "-" * 20
					print "Game Over Man, Game Over."
					print "-" * 20
					break

				if enemy.health > 0:
					print "-" * 20
					print "The {0} ({1}) attacks".format(enemy.name, number)

					defending = None
							
					for player in good:
						if player.defend:
							defending = player
							break

					if defending is None:
						player = random.choice(good)
					else:
						player = defending

					while player.health <= 0:
						player = random.choice(good)
					if enemy.hit(player.defend):
						player.health -= 1
						print "{0} has been hit!".format(player.name)
					else:
						print "The enemy attacked {0} but missed.".format(player.name)

			for player in good:
				player.defend = False
				player.cooldown_tracker()

			# check if enemies are still alive
			if not self.combat_check(evil) or not self.combat_check(good):
				break
