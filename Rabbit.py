# Author: Jason Pinga

import Creature as c

class Rabbit(c.Creature):
	def __init__(self, xpos, ypos):
		c.Creature.__init__(self, "R", xpos, ypos)

		
