from samples.classes.node import Node as node
import json

class Graph():
    
    nodes = []

    def __init__(self, jsonFile = None):
        if (jsonFile != None):
            with open(jsonFile) as file:
               nodesRaw = json.load(file)
               i = 0
               for nodeRaw in nodesRaw:
                self.nodes.append(
                    node(
                        nodeRaw["id"], 
                        nodeRaw["closeTo"], 
                        nodeRaw["nodeType"], 
                        position=nodeRaw["position"]
                    )
                )

