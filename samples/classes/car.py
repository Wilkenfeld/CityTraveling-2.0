class Car():    

    def __init__(self, id, carType, startPoint, endPoint, length, status):
        self.id = id
        self.type = carType
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.status = status
        self.props = (id, carType, startPoint, endPoint, length, status)
        self.path = []

        self.currentPosition = startPoint
        self.requestPath()

    self.position

    def requestPath(self):
