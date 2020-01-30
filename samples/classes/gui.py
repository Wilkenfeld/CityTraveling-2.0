
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
from .core import *
from .graph import Graph
from .commandsHandler import CommandHandler as handler

# Main Window
root = Tk()



def start():

    global status
    status = "start"
    

    # Creation of the main elements of the page
    cityScheme = None
    global cityModel
    cityModel = Canvas(master=root, 
                            bg="grey", 
                            width="500", 
                            height="500")

    menu = Frame(master=root, borderwidth=3, height="500", width="100", pady="30", padx="30")
    title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
    JSONMenu = Button(master = menu, text="Open File", padx="5", pady="5", command=openJSONFile)
    runButton = Button(master = menu, text="Run", padx="5", pady="5", command=run)

    global carsMenu
    carsMenu = Frame(master = root, bg ="black", width="500")
    global carsList
    carsList = Frame(master = carsMenu, bg = "green", width="500")
    global manageBar
    manageBar = Frame(master = carsMenu, bg = "blue", width = "500")

    # Layout of the window
    root.title("CitySim")
    title.pack(side="top")
    JSONMenu.pack(side="top")
    runButton.pack()

    # centers the menu
    root.grid_columnconfigure(1, weight="1")

    cityModel.grid(column="0", row="0")
    menu.grid(column="1", row="0")

    carsMenu.columnconfigure(0, weight=1)
    carsMenu.grid(column="0", row="1", sticky="NSEW")
    carsList.grid(column="0", row="0", sticky="NSEW")
    manageBar.grid(column="0", row="1", sticky="NSEW")

    root.grid_propagate(True)
    root.resizable(True, True)
    root.geometry("1200x680")
    
    # Execution
    root.mainloop()

def createPositionsDictionary():

    # Positions of the nodes on the plot
    global position_dict
    position_dict = dict()

    # Adds the values to the dictionary
    for node in graph_obj.nodes:
        position_dict[node.id] = node.position

# Gets the JSON file
def openJSONFile():
    JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                    filetypes=[("JSON Files", ".json")])
    global graph_obj
    graph_obj = Graph(JSONFilePath)
    createPositionsDictionary()

    createCityImage()
    createCarsMenu()

def createCityImage():
    # The dimension of the widget is calculated by x * dpi and y * dpi
    global fig
    fig = Figure(figsize=(5, 5), dpi=100)
    global sp
    sp = fig.add_subplot(111)

    sp.plot([n.position[0] for n in graph_obj.nodes], [n.position[1] for n in graph_obj.nodes], 'ro')

    # Draws the streets
    for node in graph_obj.nodes:
        
        targets = [position_dict[node.closeTo[i][0]] for i, _ in enumerate(node.closeTo)]

        for t in targets:
            l = lines.Line2D([node.position[0], t[0]], [node.position[1], t[1]])
            sp.add_line(l)  
            
    # Draws the nodes
    sp.plot([n.position[0] for n in graph_obj.nodes], [n.position[1] for n in graph_obj.nodes], 'ro')

    # Binds the city to a tkinter widget and draws it
    global canvas 
    canvas = FigureCanvasTkAgg(fig, master=cityModel)
    canvas.get_tk_widget().grid(column=0, row=0)   
    
    canvas.draw()


def run():
    global status
    status = "running"
    anim()

def createCarsMenu():
    # creates the header of the table
    headers = ["Car Number", "Type", "Start", "Destination", "Length", "Status"]
    for i, head in enumerate(headers):

        tmp = Label(master=carsList, text=head, bg = "white", borderwidth=1, relief="groove")
        carsList.columnconfigure(i, weight=1)
        tmp.grid(column = i, row = 0, sticky="NSEW")

    global void
    void = Label(master = carsList, text="Click Add to add a new car!")
    void.grid(row = 0, column = 0, columnspan=len(headers))

    # creates the "user" bar
    global buttons
    buttons = []
    headers = ["Play", "Pause", "Add", "Cancel", "Save", "Load"]

    for i, head in enumerate(headers):
        buttons.append({
            "command": head,
            "button": Button(master = manageBar, text = head, command = partial(handler.handleCommand, head, ))
        })
        manageBar.columnconfigure(i, weight=1)
        buttons[i]["button"].grid(row=0, column = i, sticky="NSEW")

def anim():
    # if the simulation is running
    # runs the animation\
    isRunning = status == "running"
    global animID
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
    print("draw")
    print(frame)
    rect = sp.add_patch(rect((2, 2), 1, 1))
    return rect,

# inserts cars in the table (called when a file is loaded or when the Add button is pressed)
def addCar():
    void.destroy()

    for i, car in enumerate(cars):
        for j, prop in enumerate(car.props):
            tmp = Label(master = carsList, text=prop, borderwidth="1", relief = "sunken", pady="5")
            tmp.columnconfigure(j, weight = 1)
            tmp.grid(row = i + 1, column = j, sticky="NSEW")
            # sp.add_patch(rect((2,2), car.length, car.length))
            canvas.draw()

