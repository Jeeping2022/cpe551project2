# Author: Jason Pinga

import Creature as c

class Captain(c.Creature):
	def __init__(self, xpos, ypos):
		c.Creature.__init__(self, "V", xpos, ypos)
		self.__basket = []
		
	def addVeggie(self, veg):
		self.__basket.append(veg)
	
	def setbasket(self, x): 
		# for testing
		self.__basket = x
			
	def getbasket(self):
		return self.__basket
		
