import math

class Road():

    def __init__(self, start, end, maxPollution = None):
        self.start = start
        self.end = end
        self.maxPollution = maxPollution

        self.actualPollution = 0
        self.actualSpaceLeft = math.sqrt(int(start)**2 + int(end)**2)

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
    