class Node():
    
    def __init__(self, id = None, closeTo = None, nodeType = None, position = None):
        self.id = id
        self.closeTo = closeTo
        self.position = tuple(position)
        self.nodeType = nodeType
        
    
