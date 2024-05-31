import math
class Circle:
  def __init__(self, r):
    self.r = r

  def calculate_area(self):
    return math.pi * self.r * self.r
circle = Circle(float(input("RADIUS OF THE CIRCLE: ")))
area = circle.calculate_area()
print("AREA", area)