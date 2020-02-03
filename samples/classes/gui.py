
import math as Math
from functools import partial
from tkinter import *
import tkinter
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
root = Tk()

def start():
    # initialization of the common elements
    core.initialize()
    cityScheme = None
    core.cityModel = Canvas(master=root, 
                            bg="grey", 
                            width="500", 
                            height="500")

    menu = Frame(master=root, borderwidth=3, height="500", width="100", pady="30", padx="30")
    title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
    JSONMenu = Button(master = menu, text="Open File", padx="5", pady="5", command=openJSONFile)
    runButton = Button(master = menu, text="Run", padx="5", pady="5", command=run)

    carsMenu = Frame(master = root, bg ="black", width="500")
    core.carsList = Frame(master = carsMenu, bg = "green", width="500")
    core.manageBar = Frame(master = carsMenu, bg = "blue", width = "500")

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
    fig = Figure(figsize=(5, 5), dpi=100)
    sp = fig.add_subplot(111)

    sp.plot([n.position[0] for n in core.graph_obj.nodes], [n.position[1] for n in core.graph_obj.nodes], 'ro')

    # Draws the streets
    for node in core.graph_obj.nodes:
        
        targets = [core.position_dict[node.closeTo[i][0]] for i, _ in enumerate(node.closeTo)]

        for t in targets:
            l = lines.Line2D([node.position[0], t[0]], [node.position[1], t[1]])
            sp.add_line(l)  
            
    # Draws the nodes
    sp.plot([n.position[0] for n in core.graph_obj.nodes], [n.position[1] for n in core.graph_obj.nodes], 'ro')

    # Binds the city to a tkinter widget and draws it 
    canvas = FigureCanvasTkAgg(fig, master=core.cityModel)
    canvas.get_tk_widget().grid(column=0, row=0)   
    
    canvas.draw()


def run():
    status = "running"
    anim()

def createCarsMenu():
    # creates the header of the table
    headers = ["Car Number", "Type", "Start", "Destination", "Length", "Status"]
    for i, head in enumerate(headers):

        tmp = Label(master=core.carsList, text=head, bg = "white", borderwidth=1, relief="groove")
        core.carsList.columnconfigure(i, weight=1)
        tmp.grid(column = i, row = 0, sticky="NSEW")

    core.void = Label(master = core.carsList, text="Click Add to add a new car!")
    core.void.grid(row = 0, column = 0, columnspan=len(headers))

    # creates the "user" bar
    buttons = []
    headers = ["Play", "Pause", "Add", "Cancel", "Save", "Load"]

    for i, head in enumerate(headers):
        buttons.append({
            "command": head,
            "button": Button(master = core.manageBar, text = head, command = getCars())
        })
        core.manageBar.columnconfigure(i, weight=1)
        buttons[i]["button"].grid(row=0, column = i, sticky="NSEW")

def getCars():
    pass

def anim():
    # if the simulation is running
    # runs the animation\
    isRunning = status == "running"
    
    animID = animation.FuncAnimation(fig, draw, frames=500, interval=20, blit=True)

    print ("status: " + status)
    print("fig: ", fig)
    print("animID:", animID)
    print("draw:", draw)
    if isRunning:
        print("animation started")
    else: 
        print("animation stopped")

def draw(frame):
    rectangle = sp.add_patch(rect((2 * (frame / 50), 2 * (frame / 100)), 1, 1))
    cars_coords = calc_coords()
    return rectangle,

# inserts cars in the table (called when a file is loaded or when the Add button is pressed)
def addCar():
    core.void.destroy()

    for i, car in enumerate(cars):
        for j, prop in enumerate(car.props):
            tmp = Label(master = core.carsList, text=prop, borderwidth="1", relief = "sunken", pady="5")
            tmp.columnconfigure(j, weight = 1)
            tmp.grid(row = i + 1, column = j, sticky="NSEW")
            canvas.draw()

def calc_coords():
    for car in cars:
        car.getCurrentPosition()