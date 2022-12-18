

class Question4:

    def __init__(self):
        self.f = 10
        self.m1 = 2
        self.m2 = 3
        self.a = self.findA()

    def findA(self):
        return round(self.f/(self.m1+self.m2))

    def findFs(self):
        return round(self.m2*self.a)
