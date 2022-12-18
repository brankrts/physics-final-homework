

class Question3:
    def __init__(self):
        self.m1 = 6
        self.m2 = 4
        self.g = 9.8

    def findA(self):

        return round(self.g*((self.m1-self.m2)/(self.m1+self.m2)), 2)

    def findTfirst(self):

        return round(self.m2*self.findA() + self.m2*self.g, 2)

    def findTend(self):
        return round(self.m1 * self.g, 2)
