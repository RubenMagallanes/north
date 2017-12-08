
class Player:
	name=""
	number=0
	hp = 5
	
	equiment = []

	def __init__(self, number, name):
		self.number = number
		self.name = name
		
	def equip(self, item):
		equipment.append(item)

