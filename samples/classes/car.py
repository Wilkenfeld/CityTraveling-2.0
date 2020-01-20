class Car():    

    def __init__(self, ID, carType, startPoint, endPoint, length, status):
        self.id = ID
        self.type = carType
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.length = length
        self.status = status
        self.props = (ID, carType, startPoint, endPoint, length, status)
        self.path = []

        self.currentPosition = startPoint

    def requestPath(self):
        pass
