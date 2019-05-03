"""
497 random point in non-overlapping rectangles
"""

from bisect import bisect_left
from random import randint

class Solution:
  def __init__(self, rects):
    self.rects = rects
    self.ranges = []
    # compute the accumulated sum
    sums = 0
    for x1, y1, x2, y2 in self.rects:
      sums += (x2-x1+1) * (y2-y1+1)
      self.ranges.append(sums)

  def pick(self):
    # select the rectangle first, then select the point
    x1, y1, x2, y2 = self.rects[bisect_left(self.ranges, randint(1, self.ranges[-1]))]
    return (randint(x1, x2), randint(y1, y2))