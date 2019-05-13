"""
478 generate random point in a circle
"""

import random
class Solution:
  def __init__(self, x_center, y_center, radius):
    self.x_center, self.x_min, self.x_max = x_center, x_center-radius, x_center+radius
    self.y_center, self.y_min, self.y_max = y_center, y_center - radius, y_center+radius
    self.radius = radius

  def randPoint(self):
    # generate the random point inside (x_min, x_max) and (y_min, y_max) and return the point if it is inside the circle
    while True:
      x, y = random.uniform(self.x_min, self.x_max), random.uniform(self.y_min, self.y_max)
      if (x-self.x_center) ** 2 + (y-self.y_center) ** 2 <= self.radius ** 2:
        return [x, y]
