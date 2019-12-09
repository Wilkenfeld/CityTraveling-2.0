import math as Math
import samples.classes.core as core
from tkinter import *
from tkinter import filedialog
import samples.classes.graph as graph

# Main Window
root = Tk()

class GUI():

    coords = []

    def main(self):
        
        # Creation of the main elements of the page
        cityScheme = graph.Graph()
        cityModel = Canvas(master=root, bg="grey", width=500, height=680)
        menu = Frame(master=root, borderwidth=3, height="680", width="700", padx="200")
        title = Label(master=menu, text="CitySim! (ALPHA RELEASE 1.0)")
        JSONMenu = Button(master=menu, text="Open File", padx="5", pady="5", command=self.openJSONFile)


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
        self.JSONFilePath = filedialog.askopenfilename(title="Select JSON file", 
                                                        filetypes=[("JSON Files", ".json")])

    # Calcs the proportions (in units) to draw nodes & links
    def calcCoords(self, graph):

        # Default values for the first node
        nodeCenter = (core.nodeDimension, core.nodeDimension)
        distance = 0

        for node in graph.nodes:

            # Checks if the node exists
            for x in self.coords:
                avoid = False
                if x["id"] == node.id:
                    avoid = True       

                if avoid is False:
                    # Coords of the center of the node
                    hor = abs(Math.cos(distance) * distance) % core.canvasDimensions[0]
                    ver = abs(Math.sin(distance) * distance) % core.canvasDimensions[1]
                    
                    coords = {
                        "id": node.id,
                        "nodeCenter": nodeCenter,
                        "type": node.type
                    }
                    
                    self.coords.append(coords)

                    for close in node.closeTo:
                        pass