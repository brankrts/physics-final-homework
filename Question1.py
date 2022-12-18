
import math


class Question1:

    def __init__(self):
        self.PI_RADYAN = 180

    def solve(self, vectors):

        Adegre = self.findArea(
            vectors[0]['area'], vectors[0]['degree'])
        Bdegre = self.findArea(
            vectors[1]['area'], vectors[1]['degree'])
        Cdegre = self.findArea(
            vectors[2]['area'], vectors[2]['degree'])

        Ax, Ay = self.findComponents(
            vectors[0]['length'], Adegre)
        Bx, By = self.findComponents(
            vectors[1]['length'], Bdegre)
        Cx, Cy = self.findComponents(
            vectors[2]['length'], Cdegre)

        Rx, Ry = self.findResultant([Ax, Ay], [Bx, By], [Cx, Cy])
        R = complex(Rx, Ry)

        return round(self.findSizeOfResultant(R), 2), round(self.findDegree(R))

    def findDegree(self, R):
        return math.degrees(math.atan(R.imag/R.real))

    def findArea(self, area, degree):
        if area == 1:
            return degree
        elif area == 2:
            return self.PI_RADYAN - degree
        elif area == 3:
            return self.PI_RADYAN + degree
        else:
            return 2*self.PI_RADYAN - degree

    def findComponents(self, length, degree):

        x = round(math.cos(math.radians(degree))*length, 2)
        y = round(math.sin(math.radians(degree))*length, 2)
        return x, y

    def findResultant(self, A, B, C):
        Rx = A[0] + B[0] + C[0]
        Ry = A[1] + B[1] + C[1]

        return Rx, Ry

    def findSizeOfResultant(self, R):
        Rsize = (((R.real)**2) + ((R.imag)**2))**(1/2)
        return Rsize
