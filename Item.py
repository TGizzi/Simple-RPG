class Item:
	def __init__(self, itemName):
		self.name = itemName
		if itemName == "Medkit":
			self.appearance = "A white box with a red cross"
			self.actionDescription = "Heals a party member"
		elif itemName == "Grenade":
			self.appearance = "Looks like a turtle-ish egg or something"
			self.actionDescription = "Damages all enemies"

class ItemList:
		Medkit = Item("Medkit")
		Grenade = Item("Grenade")
