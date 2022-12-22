
from Question1 import *


class Question5:

    def __init__(self):
        self.q1 = Question1()
        self.width = 60
        self.Vn = 4
        self.V1, self.V2 = 10, 10
        self.V1d, self.V2d = self.findDegree()
        self.V1x, self.V1y, self.V2x, self.V2y = self.findComponents()[0][0], self.findComponents()[
            0][1], self.findComponents()[1][0], self.findComponents()[1][1]
        self.t1, self.t2 = self.findT()
        self.x1, self.x2 = self.findTotalRoadTaken()
        self.distance = self.findDistance()

    def findDegree(self):
        return self.q1.findArea(2, 50), self.q1.findArea(1, 30)

    def findComponents(self):
        return self.q1.findComponents(self.V1, self.V1d), self.q1.findComponents(self.V2, self.V2d)

    def findT(self):
        return self.width/self.V1y, self.width/self.V2y

    def findTotalRoadTaken(self):
        return (self.V1x+self.Vn)*self.t1, (self.V2x+self.Vn)*self.t2

    def findDistance(self):
        return round(self.x2 - self.x1, 2)
