from math import pi

class GeometryTools:
    def rectangleArea(self, a, b):
        return a*b
    def rectanglePerimeter(self, a, b):
        return (2*a) + (2*b)
    def triangleArea(self, a, b):
        return (a*b)/2
    def trianglePerimeter(self, a, b, c):
        return a+b+c    
    def circleArea(self, r):
        return 3.14*r*r
    def circlePerimeter(self, r):
        return 2*3.14*r