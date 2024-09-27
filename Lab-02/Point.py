import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"
    def distanceto(self, otherpoint):
        dx = self.x - otherpoint.x
        dy = self.y - otherpoint.y
        return math.sqrt(dx**2+dy**2)
    
def main():
    a = Point(3,2)
    b = Point(-1,5)
    print(a)
    print("I have two point objects: " + str(a) + " " + str(b))
    howfar = a.distanceto(b)
    print(howfar)

    a = Point(0,0)
    b = Point(1,1)
    print("Distance from " + str(a) + " to " + str(b) + " is " + str(a.distanceto(b)))

if __name__ == "__main__":
    main()