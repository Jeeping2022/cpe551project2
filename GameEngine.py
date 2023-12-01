# Author: Christian O'Connell
# Date: 12/1/2023
# Description: Drives the core game functionality

import os
import random
from Veggie import Veggie

NUMBEROFVEGGIES = 30
NUMBEROFRABBITS = 5
HIGHSCOREFILE = "highscore.data"

class GameEngine:
    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__captain = None
        self.__vegetables = [] #represents all possible vegetables in the game
        self.__score = 0

    def initVeggies(self):
        fileFound = False
        while(not fileFound):
            vegFilePath = input("Enter the name of the veggie file: ")
            fileFound = os.path.exists(vegFilePath)
        vegFile = open(vegFilePath)
        firstLine = vegFile.readline().strip().split(",")
        fieldHeight = int(firstLine[1])
        fieldWidth = int(firstLine[2])

        for i in range(fieldWidth):
            arr = []
            for j in range(fieldHeight):
                arr.append(None)
            self.__field.append(arr)

        for line in vegFile:
            vegLine = line.strip().split(",")
            newVeg = Veggie(vegLine[1],vegLine[0],vegLine[2])
            self.__vegetables.append(newVeg)

        vegFile.close()
        count = 0
        while(count < NUMBEROFVEGGIES):
            randPos = random.randint(0, fieldWidth*fieldHeight)
            if(self.__field[randPos // fieldWidth][randPos % fieldWidth] == None):
                self.__field[randPos // fieldWidth][randPos % fieldWidth] = self.__vegetables[random.randint(0, len(self.__vegetables))]
                # selects random position and puts a random vegetable there (if that position is open)
                count += 1