# This file contains all of the global variables needed, such as the list of cars


def initialize():

    # Widgets
    global cityModel
    global carsMenu
    global carsList
    global manageBar
    global void

    # handler for the animation
    global animID
    animID = None

    # Buttons of the cars list
    global buttons

    # The plot itself
    global sp

    # MPL widget containing the plot and the canvas to handle it with tkinter
    global fig
    global canvas

    # Graph object
    global graph_obj

    # Positions of the nodes on the plot
    global position_dict

    # unit to scale lines and nodes 
    # (e.g.: if unit = 3 and line = 3, the final line equals line * unit = 9)
    global unit
    unit = 3

    # Dimensions of the root (hor, ver)
    global dimensions
    dimensions = (1200, 800)

    # Dimension of the canvas (hor, ver)
    global canvasDimensions
    canvasDimensions = (800, 800)

    # List of cars on the simulation
    global cars_common
    cars_common = []

    # Status of the app (at the beginning is setted on "start")
    global status
    status = "start"