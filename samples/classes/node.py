class Node():
    closeTo = []
    id = int
    data = {}
    
    def __init__(self, id = None, closeTo = None, nodeType = None, position = None):
        self.id = id
        self.closeTo = closeTo
        self.position = tuple(position)
        
    
