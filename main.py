# Author: Christian O'Connell
# Date: 12/8/2023
# Description: Drives GameEngine class to manage the game

from GameEngine import GameEngine

def main():
    ge = GameEngine()
    ge.initializeGame()
    ge.intro()
    numVegLeft = ge.remainingVeggies()
    score = 0
    while(numVegLeft > 0):
        score = ge.getScore()
        print(f"{numVegLeft} veggies remaining. Current score: {score}")
        ge.printField()
        ge.moveRabbits()
        ge.moveCaptain()
        ge.moveSnake()
        numVegLeft = ge.remainingVeggies()
    # game ends when no veggies remain
    ge.gameOver()
    ge.highScore()

main()
