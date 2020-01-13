class Road():

    def __init__(self, start, end, maxPollution, length):
        self.start = start
        self.end = end
        self.maxPollution = maxPollution
        self.length = length

        self.actualPollution = maxPollution
        self.actualSpaceLeft = length                
    
    def addCar(self, car):
        isAcceptable = self.actualSpaceLeft >= car.length and self.actualPollution + car.pollution < self.maxPollution
        if isAcceptable:
            self.actualSpaceLeft -= car.length
            self.actualPollution += car.pollution
            return True
        else:
            return None

    def removeCar(self, car):
        self.actualPollution -= car.pollution
        self.actualSpaceLeft += car.length
    