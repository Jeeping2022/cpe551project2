# Author: Jason Pinga

import Creature as c

class Snake(c.Creature):
	def __init__(self, xpos, ypos):
		c.Creature.__init__(self, "S", xpos, ypos)
