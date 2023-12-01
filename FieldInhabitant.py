# Author: Jason Pinga

class FieldInhabitant():
	def __init__(self, symbol):
		self._symbol = str(symbol)
		
	def setsymbol(self, x):
		self._symbol = str(x)
			
	def getsymbol(self):
		return self._symbol