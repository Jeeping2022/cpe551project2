# Author: Jason Pinga

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
	def __init__(self, symbol, xpos, ypos):
		FieldInhabitant.__init__(self, symbol)
		self._xpos = int(xpos)
		self._ypos = int(ypos)
		
	def setxpos(self, x):
		self._xpos = int(x)
			
	def getxpos(self):
		return self._xpos
		
	def setypos(self, x):
		self._ypos = int(x)
			
	def getypos(self):
		return self._ypos