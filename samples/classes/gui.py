
import math as Math
from functools import partial
import tkinter as tk
from tkinter import filedialog
import matplotlib as mpl
import json
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import matplotlib.lines as lines
from matplotlib.patches import Rectangle as rect
import matplotlib.animation as animation

# Custom imports
import samples.classes.core as core
from .graph import Graph
from .commandsHandler import CommandHandler as handler

# Main Window
root = tk.Tk()


def start():
    # initialization of the common elements
    core.initialize()
    cityScheme = None
    core.cityModel = tk.Canvas(master=root, 
                            bg="grey", 
                            width="500", 
                            height="500")

    menu = tk.Frame(master=root, borderwidth=3, height="500", width="100", pady="30", padx="30")
    title = tk.Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
    JSONMenu = tk.Button(master = menu, text="Open File", padx="5", pady="5", command=openJSONFile)
    runButton = tk.Button(master = menu, text="Run", padx="5", pady="5", command=run)

    carsMenu = tk.Frame(master = root, bg ="black", width="500")
    core.carsList = tk.Frame(master = carsMenu, bg = "green", width="500")
    core.manageBar = tk.Frame(master = carsMenu, bg = "blue", width = "500")

    # Layout of the window
    root.title("CitySim")
    title.pack(side="top")
    JSONMenu.pack(side="top")
    runButton.pack()

    # centers the menu
    root.grid_columnconfigure(1, weight="1")

    core.cityModel.grid(column="0", row="0")
    menu.grid(column="1", row="0")

    carsMenu.columnconfigure(0, weight=1)
    carsMenu.grid(column="0", row="1", sticky="NSEW")
    core.carsList.grid(column="0", row="0", sticky="NSEW")
    core.manageBar.grid(column="0", row="1", sticky="NSEW")

    root.grid_propagate(True)
    root.resizable(True, True)
    root.geometry("1200x680")

    # Execution
    root.mainloop()

def createPositionsDictionary():
    core.position_dict = dict()

    # Adds the values to the dictionary
    for node in core.graph_obj.nodes:
        core.position_dict[node.id] = node.position

# Gets the JSON file
def openJSONFile():
    JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                    filetypes=[("JSON Files", ".json")])
    core.graph_obj = Graph(JSONFilePath)
    createPositionsDictionary()

    createCityImage()
    createCarsMenu()

def createCityImage():
    
    # The dimension of the widget is calculated by x * dpi and y * dpi
    core.fig = Figure(figsize=core.canvasDimensions, dpi=100)
    core.sp = core.fig.add_subplot(111)
    # core.sp.set_axes_off()

    core.sp.plot([n.position[0] for n in core.graph_obj.nodes], [n.position[1] for n in core.graph_obj.nodes], 'ro')

    # Draws the streets
    for node in core.graph_obj.nodes:
        
        targets = [core.position_dict[node.closeTo[i][0]] for i, _ in enumerate(node.closeTo)]
        # print (node.closeTo[0][0])
        for t in targets:
            l = lines.Line2D([node.position[0], t[0]], [node.position[1], t[1]])
            core.sp.add_line(l)
            
    # Draws the nodes
    core.sp.plot([n.position[0] for n in core.graph_obj.nodes], [n.position[1] for n in core.graph_obj.nodes], 'ro')

    # Binds the city to a tkinter widget and draws it 
    core.canvas = FigureCanvasTkAgg(core.fig, master=core.cityModel)
    core.canvas.get_tk_widget().grid(column=0, row=0)   

    core.canvas.draw()

    # animation.FuncAnimation(core.fig, partial(tranim, i), frames = 500, interval = 200, blit=True)
 
def tranim(frame, i):
    print(i)
    x = 1
    y = 1
    x += 0.5
    y += 0.5

    prov_fig = rect((x, y), 0.6 , 0.6)
    core.sp.add_patch(prov_fig)

    return prov_fig,

def run():
    core.status = "running"
    anim()

def createCarsMenu():
    # creates the header of the table
    headers = ["Car Number", "Type", "Start", "Destination", "Length", "Status"]
    for i, head in enumerate(headers):

        tmp = tk.Label(master=core.carsList, text=head, bg = "white", borderwidth=1, relief="groove")
        core.carsList.columnconfigure(i, weight=1)
        tmp.grid(column = i, row = 0, sticky="NSEW")

    core.void = tk.Label(master = core.carsList, text="Click Add to add a new car!")
    core.void.grid(row = 0, column = 0, columnspan=len(headers))

    # creates the "user" bar
    buttons = []
    headers = ["Play", "Pause", "Add", "Cancel", "Save", "Load"]

    for i, head in enumerate(headers):
        buttons.append({
            "command": head,
            "button": tk.Button(master = core.manageBar, text = head, command = partial(getCars, head))
        })
        core.manageBar.columnconfigure(i, weight=1)
        buttons[i]["button"].grid(row=0, column = i, sticky="NSEW")

def getCars(head):
    handler.handleCommand(head)
    if (head == "Load"): 
        addCar()

def anim():
    # if the simulation is running
    # runs the animation
    isRunning = core.status == "running"

    core.animID = animation.FuncAnimation(core.fig, draw, repeat=False, frames=200, interval=20, blit=True)

    print ("status: " + core.status)
    print("fig: ", core.fig)
    print("animID:", core.animID)
    print("draw:", draw)
    if isRunning:
        print("animation started")
    else: 
        print("animation stopped")

def draw(frame):
    car_rects = []

    for i, car in enumerate(core.cars_common):
        if car.status == "running":
            details = core.graphic_cars_details[i]
            print (details["current_x"], details["current_y"])
            print(core.position_dict[str(car.path[details["next_point_index"]])])
            if (details["current_x"]  >= core.position_dict[str(car.path[details["next_point_index"]])][0] and round(details["current_y"])  == core.position_dict[str(car.path[details["next_point_index"]])][1]):
                print("nell'if")
                core.graphic_cars_details[i]["next_point_index"] += 1
                if (core.graphic_cars_details[i]["next_point_index"] < len(car.path)):
                    
                    x_inc = (core.position_dict[str(car.path[details["next_point_index"]])][0] - core.position_dict[str(car.path[details["next_point_index"] - 1])][0]) / float(200)
                    x_inc = (x_inc * 200) / car.path_length
                    
                    y_inc = (core.position_dict[str(car.path[details["next_point_index"]])][1] - core.position_dict[str(car.path[details["next_point_index"] - 1])][1]) / float(200)
                    y_inc = (y_inc * 200) / car.path_length
                    core.graphic_cars_details[i]["next_point_increase"] = (x_inc, y_inc)

                    x = round(core.graphic_cars_details[i]["current_x"])
                    y = round(core.graphic_cars_details[i]["current_y"])

                else:
                    car.status = "finished"

            else:                
                x = core.graphic_cars_details[i]["current_x"] + core.graphic_cars_details[i]["next_point_increase"][0]
                y = core.graphic_cars_details[i]["current_y"] + core.graphic_cars_details[i]["next_point_increase"][1]

            core.graphic_cars_details[i]["current_x"] = x
            core.graphic_cars_details[i]["current_y"] = y

        else:
            x = core.graphic_cars_details[i]["current_x"]
            y = core.graphic_cars_details[i]["current_y"]

        prov_fig = rect((x - 0.3, y - 0.5), 0.6 , 0.6)
        car_rects.append(prov_fig)
        
        for rec in car_rects:
            core.sp.add_patch(prov_fig)

    # rectangle = core.sp.add_patch(rect((2 * (frame / 50), 2 * (frame / 100)), 1, 1))
    # cars_coords = calc_coords()
    
    return prov_fig,

# inserts cars in the table (called when a file is loaded or when the Add button is pressed)
def addCar():
    core.void.destroy()

    for i, car in enumerate(core.cars_common):
        for j, prop in enumerate(car.props):
            tmp = tk.Label(master = core.carsList, text=prop, borderwidth="1", relief = "sunken", pady="5")
            tmp.columnconfigure(j, weight = 1)
            tmp.grid(row = i + 1, column = j, sticky="NSEW")
            core.canvas.draw()

def calc_coords():
    for car in core.cars_common:
        car.getCurrentPosition()