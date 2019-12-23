from .core import *
import json

class CommandHandler():

    # Main handler
    @staticmethod
    def handleCommand(command):
        if (command == "Add"): CommandHandler.addCar()

    # Add button (adds a car)
    @staticmethod
    def addCar():
        print(cars)
        pass