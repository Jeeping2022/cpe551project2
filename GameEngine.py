# Author: Christian O + Jason P
# Date: 12/1/2023 - 12/8/2023
# Description: Drives the core game functionality

import os
import random
from Veggie import Veggie
from Rabbit import Rabbit
from Captain import Captain
from Snake import Snake

NUMBEROFVEGGIES = 30
NUMBEROFRABBITS = 5
HIGHSCOREFILE = "highscore.data"

class GameEngine:
    def __init__(self):
        self.__field = []
        self.__rabbits = []
        self.__snake = None
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
            randPos = random.randint(0, (fieldWidth*fieldHeight) - 1)
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
        for i in range((fieldWidth*2) + 3):
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
        for i in range((fieldWidth * 2) + 3):
            textLine += "#"
        print(textLine)  # bottom border

    def initRabbits(self):
        count = 0
        fieldWidth = len(self.__field)
        fieldHeight = len(self.__field[0])
        while (count < NUMBEROFRABBITS):
            randPos = random.randint(0, (fieldWidth * fieldHeight) - 1)
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

    def initCaptain(self):
        # calc field width and field height
        fh, fw = len(self.__field[0]), len(self.__field)
        while True:
            randPos = random.randint(0, (fw*fh)-1)
            ry, rx = (randPos // fw) , (randPos % fh)
            if(self.__field[rx][ry] == None):
                c = Captain(rx, ry)
                self.__field[rx][ry] = c
                self.__captain = c
                break
            else:
                continue

    def initSnake(self):
        # calc field width and field height
        fh, fw = len(self.__field[0]), len(self.__field)
        while True:
            randPos = random.randint(0, (fw*fh)-1)
            ry, rx = (randPos // fw) , (randPos % fh)
            if(self.__field[rx][ry] == None):
                s = Snake(rx, ry)
                self.__field[rx][ry] = s
                self.__snake = s
                break
            else:
                continue
                
    def moveCptVertical(self, inp):
        if self.__captain == None:
            print("No captain object found!")
        else:
            # 1 is down, -1 is up
            move = 1 if (inp > 0) else -1
            # initiate location and destination
            oldpos = [self.__captain.getxpos(), self.__captain.getypos()]
            newpos = [self.__captain.getxpos()][self.__captain.getypos() + move]
            # object at the destination
            target = self.__field[newpos[0]][newpos[1]]
            if target == None:
                # update field
                self.__field[newpos[0]][newpos[1]] = self.__captain 
                self.__field[oldpos[0]][oldpos[1]] = None
                # update captain
                self.__captain.setypos(self.__captain.getypos() + move)
            elif isinstance(target, Veggie):
                # update field
                self.__field[newpos[0]][newpos[1]] = self.__captain 
                self.__field[oldpos[0]][oldpos[1]] = None
                # update captain
                self.__captain.setypos(self.__captain.getypos() + move)
                
                name, worth = target.getname(), target.getworth()
                print("Captain has picked up a delicious", name, "from the field!")
                self.__captain.addVeggie(target)
                self.__score += worth
            elif isinstance(target, Rabbit):
                x = "up" if move == 1 else "down"
                print("Can't move " + x + "; Don't step on the rabbits!")
                
    def moveCptHorizontal(self, inp):
        if self.__captain == None:
            print("No captain object found!")
        else:
            # 1 is right, -1 is left
            move = 1 if (inp > 0) else -1
            # initiate location and destination
            oldpos = [self.__captain.getxpos(), self.__captain.getypos()]
            newpos = [self.__captain.getxpos() + move][self.__captain.getypos()]
            # object at the destination
            target = self.__field[newpos[0]][newpos[1]]
            if target == None:
                # update field
                self.__field[newpos[0]][newpos[1]] = self.__captain 
                self.__field[oldpos[0]][oldpos[1]] = None
                # update captain
                self.__captain.setxpos(self.__captain.getxpos() + move)
            elif isinstance(target, Veggie):
                # update field
                self.__field[newpos[0]][newpos[1]] = self.__captain 
                self.__field[oldpos[0]][oldpos[1]] = None
                # update captain
                self.__captain.setxpos(self.__captain.getxpos() + move)
                
                name, worth = target.getname(), target.getworth()
                print("Captain has picked up a delicious", name, "from the field!")
                self.__captain.addVeggie(target)
                self.__score += worth
            elif isinstance(target, Rabbit):
                x = "right" if move == 1 else "left"
                print("Can't move " + x + "; Don't step on the rabbits!")
                
    def moveCaptain(self):
        # calc field width and field height
        fw, fh = len(self.__field[0]), len(self.__field)
        key = input("Move the captain: Up (W), Down (S), Left (A), Right(D): ")
        k = key.lower() 
        mx, my = self.__captain.getxpos(), self.__captain.getypos()
        if (k == "W"):
            if (my - 1) >= 0:
                self.moveCptVertical(-1)
            else: 
                print("Going up is out of bounds!")
        elif (k == "S"):
            if (my + 1) <= (fh-1):
                self.moveCptVertical(1)
            else:
                print("Going down is out of bounds!")
        elif (k == "D"):
            if (mx + 1) <= (fw-1):
                self.moveCptHorizontal(1)
            else:
                print("Going right is out of bounds!")
        elif (k == "A"):
            if (mx - 1) >= 0:
                self.moveCptHorizontal(-1)
            else:
                print("Going left is out of bounds!")
        else:
            print("Not a valid move command:", k)


