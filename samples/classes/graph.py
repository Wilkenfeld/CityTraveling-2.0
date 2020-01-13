from .node import Node as node
import json
from road import Road
from tkinter import messagebox

class Graph():
    
    number_of_graphs = 0
    self.nodes = []
    self.roads = {}

    def __init__(self, jsonFile = None):
        if (jsonFile != None and Graph.number_of_graphs == 0):
            Graph.number_of_graphs += 1

            with open(jsonFile) as file:
                try:
                    nodesRaw = json.load(file)
                    for nodeRaw in nodesRaw:
                        self.nodes.append(
                            node(
                                nodeRaw["id"], 
                                nodeRaw["closeTo"], 
                                nodeRaw["nodeType"], 
                                position = nodeRaw["position"]
                            )
                        )

                        for node in nodeRaw["closeTo"]:
                            self.roads[nodeRaw["id"]] = Road(nodeRaw["id"], node[0], node[2], node[1])

                except:
                    messagebox.showerror("Error loading the file", "This file is not a city configuration file")            

    # Creates a path
    def makePath(self, start, end, car):
        outOfPollutionLimit = False
        nodeID = start
        path = []
        while nodeID is not end and not outOfPollutionLimit:
            while not outOfPollutionLimit or nodeID is not end:
                if node.id not in path:
                    possible = []
                    for road in roads[node.id]:
                        if (road.actualSpaceLeft >= car.length and road.actualPollution + car.pollution < road.maxPollution):
                            possible.append(road)
                    shorter = min([road.length for road in possible])
                    
                    

                    

