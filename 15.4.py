class Point:
    def __init__(self, newX, newY):
      self.x = newX
      self.y = newY

    def setXY(self, newX , newY):
       self.x = newX
       self.y = newY

    def getXY(self):
        return self.x, self.y


    def dist(self, p):
        from math import sqrt
        return sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2) #расстояние между точками



p = Point(0, 0)
print(p.getXY())
p.setXY(2,4)
print(p.getXY())

q = Point(1, 1)
print(q.getXY())
q.setXY(5,8)
print(q.getXY())

print(p.dist(q))
