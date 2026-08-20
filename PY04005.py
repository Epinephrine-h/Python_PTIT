import sys
import math
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
class Triangle:
    def __init__(self, p1, p2, p3):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    def get_perimeter(self):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)
        if a + b <= c or a + c <= b or b + c <= a:      return "INVALID"
        return f"{a+b+c:.3f}"
data = sys.stdin.read().split()
testcase = int(data[0])
idx = 1
for _ in range(testcase):
    coords = [float(d) for d in data[idx:idx+6]]
    idx += 6
    p1 = Point(coords[0], coords[1])
    p2 = Point(coords[2], coords[3])
    p3 = Point(coords[4], coords[5])
    x = Triangle(p1, p2, p3)
    print(x.get_perimeter())