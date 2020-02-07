import samples.classes.core as core
import json
import tkinter as tk
import matplotlib.pyplot as plt
from .car import Car
import traceback as tb
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

class CommandHandler():
    # Main handler
    @staticmethod
    def handleCommand(command):
        if (command == "Add"): CommandHandler.addCar()
        elif command == "Load": CommandHandler.loadFromFile()

    # Add button (adds a car)
    @staticmethod
    def addCar(car):
        core.graphic_cars_details.append({
            "current_x": core.position_dict[str(car.startPoint)][0],
            "current_y": core.position_dict[str(car.startPoint)][1],
            "next_point_index": 0,
            "next_point_increase": (0, 0)
        })
        core.cars_common.append(car)
        print(car)

    @staticmethod
    def loadFromFile():
        JSONFilePath = tk.filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])
        # loads the cars from the JSON file
        with open(JSONFilePath) as file:
            try:
                listOfCars = json.load(file)
                    
                for car in listOfCars:
                    car_obj = Car(car["id"], car["type"], car["startPoint"], car["endPoint"], car["length"], car["status"], car["pollution"])
                    car_obj.requestPath()
                    CommandHandler.addCar(car_obj)

            except Exception as e:
                tb.print_exc()
                tk.messagebox.showerror("Error loading the file", "The current file isn't a car configuration file")
