import samples.classes.node as node
import json

class Graph():
    
    nodes = []

    def __init__(self, jsonFile = None):
        if (jsonFile != None):
            with open(jsonFile) as file:
               nodesRaw = json.load(file)
               i = 0
               for nodeRaw in nodesRaw:
                self.nodes[i] = node(nodeRaw["id"], nodeRaw["closeTo"], nodeRaw["nodeType"])

