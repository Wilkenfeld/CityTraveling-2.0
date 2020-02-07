import samples.classes.core as core
class Car():    

    def __init__(self, ID, carType, startPoint, endPoint, length, status, pollution):
        self.id = ID
        self.type = carType
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.length = length
        self.status = status
        self.pollution = pollution
        self.nextPoint = None
        self.props = (ID, carType, startPoint, endPoint, length, status)
        self.path = []

        self.currentPosition = startPoint
    def requestPath(self):
        self.path = core.graph_obj.makePath(self.startPoint, self.endPoint, self)


    def getCurrentPosition(self):
        return self.currentPositions
