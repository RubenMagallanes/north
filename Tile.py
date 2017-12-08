
class Tile:
	on = "nothing"
	kind = ""

	def __init__(self, kind):
		self.kind = kind

	def canMoveOnTo(self):
		if self.kind == "wall":
			return False
		if self.on == "nothing":
			return True
		return False
		
	def putOn(self, what):
		if self.canMoveOnTo():
			self.on = what
			return "successfully moved " + what.name
		return "cannot move on to this tile"

	def toSymbol(self):
		if self.on == "nothing":
			if self.kind == "wall":
				return '\u2588'	#ascii box
			if self.kind == "floor":
				return '.'
		return self.on.toSymbol()
