from math import sqrt

class Line:
  def __init__(self, pointx, pointy, otherPointx, otherPointy):
    self.__point = [pointx, pointy]
    self.__otherPoint = [otherPointx, otherPointy]

  def lineLength(self):
    return sqrt((self.__point[0] - self.__otherPoint[0]) ** 2 + (self.__point[1] - self.__otherPoint[1]) ** 2)

line = Line(3, 4, 1, 2)
print(line.lineLength())