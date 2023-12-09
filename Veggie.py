# Author: Jason Pinga

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
	def __init__(self, symbol, name, worth):
		FieldInhabitant.__init__(self, symbol)
		self.__name = str(name)
		self.__worth = int(worth)
		
	def __str__(self):
		return f"{self._symbol}: {self.__name} {self.__worth} points"
		
	def setname(self, x):
		self.__name = str(x)
			
	def getname(self):
		return self.__name
		
	def setworth(self, x):
		self.__worth = int(x)
			
	def getworth(self):
		return self.__worth
