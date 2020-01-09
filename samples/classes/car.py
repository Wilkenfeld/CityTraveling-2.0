class Car():

    def __init__(self, id, carType, startPoint, endPoint, status):
        self.id = id
        self.type = carType
        self.startPoint = startPoint
        self.endPoint = endPoint
        self.status = status
        self.props = (id, carType, startPoint, endPoint, status)
