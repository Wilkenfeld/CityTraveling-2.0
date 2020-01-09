from .core import *
import json
import tkinter as tk
from .car import Car

class CommandHandler():
    gui = None
    # Main handler
    @staticmethod
    def handleCommand(command, gui):
        CommandHandler.gui = gui 
        if (command == "Add"): CommandHandler.addCar()
        elif command == "Load": CommandHandler.loadFromFile()

    # Add button (adds a car)
    @staticmethod
    def addCar():
        print(cars)
        pass

    @staticmethod
    def loadFromFile():
        JSONFilePath = tk.filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])
        
        # loads the cars from the JSON file
        try:
            with open(JSONFilePath) as file:
                listOfCars = json.load(file)
                for car in listOfCars:
                    cars.append(
                        Car(car["id"], car["type"], car["startPoint"], car["endPoint"], car["status"])
                    )
            CommandHandler.gui.addCar()
                
        except Exception as e:
            print(e)
            tk.messagebox.showerror("Error loading the file", "The current file isn't a car configuration file")