class Item:
	def __init__(self, itemName, count = 1):
		self.name = itemName
		self.count = count
		if itemName == "Medkit":
			self.appearance = "A white box with a red cross"
			self.actionDescription = "Heals a party member"
		elif itemName == "Grenade":
			self.appearance = "Looks like a turtle-ish egg or something"
			self.actionDescription = "Damages all enemies"

class ItemList:
		@staticmethod
		def Medkit(count = 1):
			return Item("Medkit", count)
		@staticmethod
		def Grenade(count = 1):
			return Item("Grenade", count)
