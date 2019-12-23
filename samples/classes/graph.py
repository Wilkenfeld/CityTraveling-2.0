from .node import Node as node
import json

class Graph():
    
    number_of_graphs = 0
    nodes = []

    def __init__(self, jsonFile = None):
        if (jsonFile != None and Graph.number_of_graphs == 0):
            Graph.number_of_graphs += 1
            with open(jsonFile) as file:
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

