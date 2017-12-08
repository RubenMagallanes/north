
from Tile import Tile
from Skeleton import Skeleton

class Area:
	tiles = []
	chars = {}
	def __init__(self):
		self.tiles = []
		self.constructMap(4)
		self.placePlayer(1)
		self.populateWithSkelly()

	def constructMap(self, height):
		self.tiles.append(Tile('wall'))
	
		for i in range(height):
			self.tiles.append(Tile("floor"))

		self.tiles.append(Tile('wall'))
	
	def placePlayer(self, tile):
		p = Player(1, "rj")
		print(self.tiles[tile].putOn(p)
		chars[p] = tile
		

	def populateWithSkelly(self):
		s = Skeleton()
		print(self.tiles[4].putOn(s))
		chars[s] = 4
		

	def printMap(self):
		text = "current area: "
		for t in self.tiles:
			text += t.toSymbol()
		print(text)
