import math as Math
from tkinter import *
import graph as Graph
#import core
from tkinter import filedialog
import samples.classes.graph as graph

# Main Window
root = Tk()

class GUI():

    graph = None

    def main(self):
        
        # Creation of the main elements of the page
        cityScheme = None
        cityModel = Canvas(master=root, bg="grey", width=500, height=680)
        menu = Frame(master=root, borderwidth=3, height="680", width="700", padx="200")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master=menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)
        runButton = Button(master=menu, text="Run", padx="5", pady="5", command=self.graph.run)


        # Layout of the window
        root.title("CitySim")
        title.pack(side="top")
        JSONMenu.pack(side="top")
        cityModel.grid(sticky="NSEW", rowspan=4)
        menu.grid(column="1", row="1", padx="30")
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
        position_dict = dict()

        # Adds the nodes to the graph
        for node in graph_obj.nodes:
            graph.add_node(node.id)

            # Adds the edges
            for link in node.closeTo:
                graph.add_edge(node.id, link[0], weight=link[1])

            # Adds the values to the dictionary
            position_dict[node.id] = node.position
            
        return graph
            
