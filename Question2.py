from Question1 import *


class Question2:

    def __init__(self):
        self.Q1 = Question1()
        self.distanceToTarget = 35
        self.degree = 35
        self.targetHeight = 2.44
        self.velocity = 20
        self.g = 9.8
        self.Vx = self.takeComponents()[0]
        self.Vy = self.takeComponents()[1]
        self.V = complex(self.Vx, self.Vy)
        self.Yfirst = 0
        self.Tx = self.flightTimeToMaxHeight()
        self.Xmax = self.maxDistance()
        self.Ttarget = self.timeOfDistanceToTarget()
        self.Yend = self.findYend()

    def takeComponents(self):
        return self.Q1.findComponents(self.velocity, self.degree)

    def flightTimeToMaxHeight(self):
        return round(self.V.imag/self.g, 2)

    def totalFlightTime(self):
        return 2*self.Tx

    def timeOfDistanceToTarget(self):
        return round(self.distanceToTarget/self.V.real, 2)

    def maxDistance(self):
        return round(self.V.real * self.totalFlightTime(), 2)

    def findYend(self):
        return (self.Yfirst + (self.Vy*self.Ttarget) - (0.5*self.g*math.pow(self.Ttarget, 2)))

    def isGoal(self):
        return (self.Yend < self.targetHeight)
