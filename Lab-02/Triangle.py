from Point import Point
from Line import Line
import math

class Triangle(Line):
    def __init__(self, p1, p2, p3):
        self.l1 = Line(p1,p2)
        self.l2 = Line(p2,p3)
        self.l3 = Line(p3,p1)
    def __str__(self):
        return "Triangle {" + str(self.l1.p1) + ", " + str(self.l2.p1) + ", " + str(self.l3.p1) + "}"
    def area(self):
        x = (self.l1.length() + self.l2.length() + self.l3.length())/2
        a = math.sqrt(x*(x - self.l1.length())*(x - self.l2.length())*(x - self.l3.length()))
        return a
    
print("---------------------------Class Triangle---------------------------")
a = Point(10,15)
b = Point(4,1)
c = Point(6,32)
tri = Triangle(a,b,c)
A = tri.area()
print("Area of ", tri, " is: ", A)