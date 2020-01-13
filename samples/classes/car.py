from roadMaker import roadMaker as RM

class Car():

    self.path = []
    

    def __init__(self, id, carType, startPoint, endPoint, length, status):
        self.id = id
        self.type = carType
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.status = status
        self.props = (id, carType, startPoint, endPoint, length, status)

        self.currentPosition = start
        self.requestPath()

    def requestPath(self):
        self.path = RM.makePath(self.startPoint, self.endPoint)
