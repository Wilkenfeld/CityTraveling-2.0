import math as Math
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
        self.cityModel = Frame(master=root, bg="grey", width="1000", height="500")
        menu = Frame(master=root, borderwidth=3, height="500", width="100", pady="30", padx="30")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master=menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)
        runButton = Button(master=menu, text="Run", padx="5", pady="5", command=self.run)

        # Layout of the window
        root.title("CitySim")
        title.pack(side="top")
        JSONMenu.pack(side="top")
        runButton.pack()
        self.cityModel.grid(row="0", column="0", sticky="N")
        
        menu.grid(row="0", column="1", padx="30", sticky="N")
        
        root.grid_propagate(False)
        root.geometry("1200x680")
        

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

        #creates nx graph
        nx_graph = self.nxGraph(graph_obj)

        # The dimension of the widget is calculated by x * dpi and y * dpi,
        # where x = figsize[0] and y = figsize[1]
        fig = Figure(figsize=(5, 5), dpi=100)
        axes = fig.add_subplot(111, xmargin=0, ymargin=0, frameon="False")

        axes.set_axis_off()
        # plt.subplots_adjust(left=-1, right=0, top=0, bottom=-1)

        canvas = FigureCanvasTkAgg(fig, master=self.cityModel)
        canvas.get_tk_widget().grid(column=0, row=0)
        
        
        #draw graph
        nx.draw_networkx(nx_graph, with_labels=True, ax=axes, pos=self.position_dict)
        
        canvas.draw()
        
        plt.draw()
        plt.show()
