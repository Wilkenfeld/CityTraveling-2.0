import math as Math
from functools import partial
from tkinter import *
import tkinter
from tkinter import filedialog
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure

# Custom imports
from .core import *
from .graph import Graph
from .commandsHandler import CommandHandler as handler

# Main Window
root = Tk()

class GUI():

    graph = None

    def main(self):
        
        # Creation of the main elements of the page
        cityScheme = None
        self.cityModel = Canvas(master=root, 
                                bg="grey", 
                                width="500", 
                                height="500")

        menu = Frame(master=root, borderwidth=3, height="500", width="100", pady="30", padx="30")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master = menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)
        runButton = Button(master = menu, text="Run", padx="5", pady="5", command=self.run)

        self.carsMenu = Frame(master = root, bg ="black", width="500")
        self.carsList = Frame(master = self.carsMenu, bg = "green", width="500")
        self.manageBar = Frame(master = self.carsMenu, bg = "blue", width = "500")

        # Layout of the window
        root.title("CitySim")
        title.pack(side="top")
        JSONMenu.pack(side="top")
        runButton.pack()

        # centers the menu
        root.grid_columnconfigure(1, weight="1")

        self.cityModel.grid(column="0", row="0")
        menu.grid(column="1", row="0")

        self.carsMenu.columnconfigure(0, weight=1)
        self.carsMenu.grid(column="0", row="1", sticky="NSEW")
        self.carsList.grid(column="0", row="0", sticky="NSEW")
        self.manageBar.grid(column="0", row="1", sticky="NSEW")

        root.grid_propagate(True)
        root.resizable(True, True)
        root.geometry("1200x680")
        

        # Execution
        root.mainloop()

    # Gets the JSON file
    def openJSONFile(self):
        JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])
        self.graph_obj = Graph(JSONFilePath)
        self.createCityImage()
        self.createCarsMenu()


    # Creates the networkx graph
    def nxGraph(self, graph_obj):
        # Creates the graph
        graph = nx.DiGraph()

        # Positions of the nodes on the plot
        self.position_dict = dict()

        # Adds the nodes to the graph
        for node in graph_obj.nodes:
            graph.add_node(node.id)
            # Adds the edges
            for link in node.closeTo:
                graph.add_edge(node.id, link[0], weight=link[1])
            
            # Adds the values to the dictionary
            self.position_dict[node.id] = node.position

        return graph

    # shows the city
    def createCityImage(self):

        #creates nx graph
        nx_graph = self.nxGraph(self.graph_obj)

        # The dimension of the widget is calculated by x * dpi and y * dpi,
        # where x = figsize[0] and y = figsize[1]
        fig = Figure(figsize=(5, 5), dpi=100)
        axes = fig.add_subplot(111, xmargin=0, ymargin=0, frameon="False")

        #draw graph
        nx.draw_networkx(nx_graph, with_labels=True, ax=axes, pos=self.position_dict)
        
        plt.margins(x = 0, y = 0, tight = True)
        axes.set_axis_off()
        fig.tight_layout(pad = 0, h_pad=0, w_pad=0)

        canvas = FigureCanvasTkAgg(fig, master=self.cityModel)
        canvas.get_tk_widget().grid(column=0, row=0)
        
        
        
        canvas.draw()


    def run(self):
        pass

    def createCarsMenu(self):
        # creates the header of the table
        headers = ["Car Number", "Type", "Start", "Destination", "Status"]
        for i, head in enumerate(headers):

            tmp = Label(master=self.carsList, text=head, bg = "white", borderwidth=1, relief="groove")
            self.carsList.columnconfigure(i, weight=1)
            tmp.grid(column = i, row = 0, sticky="NSEW")

        self.void = Label(master = self.carsList, text="Click Add to add a new car!")
        self.void.grid(row = 0, column = 0, columnspan=len(headers))

        # creates the "user" bar
        self.buttons = []
        headers = ["Play", "Pause", "Add", "Cancel", "Save", "Load"]

        for i, head in enumerate(headers):
            self.buttons.append({
                "command": head,
                "button": Button(master = self.manageBar, text = head, command = partial(handler.handleCommand, head, self))
            })
            self.manageBar.columnconfigure(i, weight=1)
            self.buttons[i]["button"].grid(row=0, column = i, sticky="NSEW")

    # inserts cars in the table (called when a file is loaded or when the Add button is pressed)
    def addCar(self):
        self.void.destroy()
        for i, car in enumerate(cars):
            for j, prop in enumerate(car.props):
                tmp = Label(master = self.carsList, text=prop, borderwidth="1", relief = "sunken", pady="5")
                tmp.columnconfigure(j, weight = 1)
                tmp.grid(row = i + 1, column = j, sticky="NSEW")
