import math as Math
from tkinter import *
import tkinter
from tkinter import filedialog
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backend_bases import key_press_handler
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,
                                               NavigationToolbar2Tk)
from matplotlib.figure import Figure
import samples.classes.core as core
import samples.classes.graph as graph
from samples.classes.graph import Graph

# Main Window
root = Tk()

class GUI():

    graph = None

    def main(self):
        
        # Creation of the main elements of the page
        cityScheme = None
        self.cityModel = Frame(master=root, bg="grey", width=500, height=680)
        menu = Frame(master=root, borderwidth=3, height="680", width="700", padx="200")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master=menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)
        runButton = Button(master=menu, text="Run", padx="5", pady="5", command=self.run)

        # Layout of the window
        root.title("CitySim")
        title.pack(side="top")
        JSONMenu.pack(side="top")
        self.cityModel.grid(sticky="NSEW", rowspan=4)
        menu.grid(column="1", row="1", padx="30")
        root.geometry("1200x680")
        runButton.pack()

        # Execution
        root.mainloop()

    # Gets the JSON file
    def openJSONFile(self):
        core.JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])
        self.graph = Graph(core.JSONFilePath)

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

    # run the example
    def run(self):
        graph_obj = Graph(".\\samples\\cities\\test.json")

        fig = Figure(figsize=(5, 4), dpi=100)
        fig.add_subplot(111).plot()

        canvas = FigureCanvasTkAgg(fig, master=self.cityModel)  # A tk.DrawingArea.
        canvas.draw()
        canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        #creates nx graph
        nx_graph = self.nxGraph(graph_obj)

        #draw graph
        nx.draw_networkx(nx_graph, with_labels=True, pos=self.position_dict)
        plt.draw()
        plt.show()
