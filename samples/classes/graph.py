from .node import Node as node
import json
from .road import Road
from tkinter import messagebox
import traceback as tb
import math
import samples.classes.core as core
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
                            if (nodeRaw["id"] not in self.roads):
                                self.roads[nodeRaw["id"]] = []
                            self.roads[nodeRaw["id"]].append(Road(nodeRaw["id"], n[0], n[1]))

                except Exception as e:
                    tb.print_exc()
                    messagebox.showerror("Error loading the file", "This file is not a city configuration file")            
                    
    def makePath(self, start, end, car):
        outOfPollutionLimit = False
        nodeID = start
        # gets the best paths (according to time) and filters them checking the pollution
        paths = self.getFastestPaths(start, end)
        final_paths = []

        for path in paths:
            current = 0
            totalPollution = 0
            temp_path = []
            for node in path:
                for road in self.roads[str(node)]:
                    if (road.end is path[current + 1]):
                        if (road.actualPollution + car.pollution < road.maxPollution):
                            totalPollution += car.pollution
                            break
                temp_path.append(node)

            final_paths.append({
                "pollution": totalPollution,
                "path": temp_path
            })

        print(path)
        pollutions = [p["pollution"] for p in final_paths]
        
        return final_paths[pollutions.index(min(pollutions))]["path"]

    # Method that calculates the total distance from a node to another
    def calc_path_length(self, path):
        tot = 0
        i = 0
        while i < len(path) - 1:
            coord_a = core.position_dict[str(path[i])]
            coord_b = core.position_dict[str(path[i + 1])]
            xa = coord_a[0]
            xb = coord_b[0]
            ya = coord_a[1]
            yb = coord_b[1]

            tot += math.sqrt(((xa - xb) ** 2) + ((ya - yb) ** 2))
            i += 1
        
        return tot 


    def getFastestPaths(self, start, end):
        paths = [
                { "27": [[1, 6, 9, 14, 16, 17, 22, 27]], "12": [[1, 6, 7, 8, 10, 11, 12]] },
                { "12": [[2, 7, 8, 10, 11, 12]], "23": [[2, 7, 8, 10, 23]] },
                { "24": [[3, 8, 10, 23, 24]], "20": [[3, 8, 10, 23, 22, 21, 20]] },
                { "18": [[4, 11, 10, 15, 13, 14, 16, 19, 18]], "5": [[4, 11, 10, 8, 7, 6, 5]] },
                { "29": [[5, 6, 9, 14, 16, 17, 22, 23, 24, 29]], "12": [[5, 6, 7, 8, 10, 11, 12]] }
            ]

        return paths[start - 1][str(end)]
