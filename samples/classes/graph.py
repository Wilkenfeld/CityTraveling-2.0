from .node import Node as node
import json
from .road import Road
from tkinter import messagebox

class Graph():
    
    number_of_graphs = 0
    nodes = []
    roads = {}

    def __init__(self, jsonFile = None):
        if (jsonFile != None and Graph.number_of_graphs == 0):
            Graph.number_of_graphs += 1

            with open(jsonFile) as file:
                try:
                    nodesRaw = json.load(file)
                    for nodeRaw in nodesRaw:
                        print(nodeRaw)
                        self.nodes.append(
                            node(
                                nodeRaw["id"], 
                                nodeRaw["closeTo"], 
                                nodeRaw["nodeType"], 
                                position = nodeRaw["position"]
                            )
                        )

                        for n in nodeRaw["closeTo"]:
                            self.roads[nodeRaw["id"]] = Road(nodeRaw["id"], n[0], n[1])

                except Exception as e:
                    print(e)
                    messagebox.showerror("Error loading the file", "This file is not a city configuration file")            
                    
    def makePath(self, start, end, car):
        outOfPollutionLimit = False
        nodeID = start
        # gets the best paths (according to time) and filters them checking the pollution
        paths = getFastestPaths(start, end)
        final_paths = []

        for path in paths:
            current = 0
            totalPollution = 0
            temp_path = []
            for node in path:
                for road in self.roads[node.id]:
                    if (road.end is path[current + 1]):
                        if (road.actualPollution + car.pollution < road.maxPollution):
                            totalPollution += car.pollution
                            break

            final_paths.append({
                "pollution": totalPollution,
                "path": temp_path 
            })

        print(path)
        pollutions = [p[pollution] for p in final_paths]
         
        return final_paths[final_paths.index(min(pollutions))]["path"]

    def getFastestPaths(start, end):
        pass
