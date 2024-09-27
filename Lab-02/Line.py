from Point import Point
import math

class Line(Point):
    def __init__(self, p1, p2):
        super().__init__(p1,p2)
        self.p1 = p1
        self.p2 = p2
    def __str__(self):
        return "(" + str(self.p1) + ", " + str(self.p2) + ")"
    def length(self):
        dx = abs(self.p2.x - self.p1.x)
        dy = abs(self.p2.y - self.p1.y)
        a = self.p2.distanceto(self.p1)
        linelength = math.sqrt(dx**2 + dy**2)
        #return "The length of the line is: " + a
        return a

def main():
    print("--------------------Class Line--------------------")
    a = Point(3,2)
    b = Point(-1,7)
    c = Line(a,b)
    distance = c.length()
    print("Length of Line ", c, " is: ", distance)

if __name__ == "__main__":
    main()