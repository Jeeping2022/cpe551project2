# Author: Christian O'Connell
# Date: 12/1/2023 and 12/6/2023
# Description: Drives the core game functionality

import os
import random
from Veggie import Veggie
from Rabbit import Rabbit

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

    def remainingVeggies(self):
        vegCount = 0
        for i in range(len(self.__field)):
            for j in range(len(self.__field[0])):
                if(isinstance(self.__field[i][j], Veggie)):
                    vegCount += 1
        return vegCount

    def printField(self):
        fieldWidth = len(self.__field)
        fieldHeight = len(self.__field[0])
        textLine = ""
        for i in range((fieldWidth*2) + 1):
            textLine+="#"
        print(textLine) # top border

        for i in range(fieldHeight):
            textLine = "# "
            for j in range(fieldWidth):
                if(self.__field[i][j] == None):
                    textLine+="  "
                else:
                    textLine+=self.__field[j][i].getsymbol() + " "
            textLine+="#"
            print(textLine)

        textLine = ""
        for i in range((fieldWidth * 2) + 1):
            textLine += "#"
        print(textLine)  # bottom border

    def initRabbits(self):
        count = 0
        fieldWidth = len(self.__field)
        fieldHeight = len(self.__field[0])
        while (count < NUMBEROFRABBITS):
            randPos = random.randint(0, fieldWidth * fieldHeight)
            if (self.__field[randPos // fieldWidth][randPos % fieldWidth] == None):
                newRabbit = Rabbit(randPos // fieldWidth, randPos % fieldWidth)
                self.__rabbits.append(newRabbit)
                self.__field[randPos // fieldWidth][randPos % fieldWidth] = newRabbit
                # selects random position and puts a rabbit there (if that position is open)
                count += 1

    def moveRabbits(self):
        fieldWidth = len(self.__field)
        fieldHeight = len(self.__field[0])
        for rab in self.__rabbits:
            xmove = random.randint(-1,1)
            ymove = random.randint(-1,1)
            newxpos = rab.getxpos() + xmove
            newypos = rab.getypos() + ymove
            if(newxpos < 0 or newxpos >= fieldWidth):
                continue # out of bounds, move is skipped
            elif(newypos < 0 or newypos >= fieldHeight):
                continue # out of bounds, move is skipped
            elif(self.__field[newxpos][newypos] == None or isinstance(self.__field[newxpos][newypos], Veggie)):
                self.__field[newxpos][newypos] = rab
                self.__field[rab.getxpos()][rab.getypos()] = None
                rab.setxpos(newxpos)
                rab.setypos(newypos)
            # if the last elif is false, then there must be a rabbit or captain in the new position
            # in that case the move is skipped so nothing needs to be implemented


