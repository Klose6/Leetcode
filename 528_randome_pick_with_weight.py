"""
528 random pick with weight
"""
from random import randint
from bisect import bisect_left

import itertools

class Solution:
  def __init__(self, w):
    self.w = w

  def pickIndex(self):
    sums = [0] * len(self.w)
    sums[0] = self.w[0]
    for i in range(1, len(self.w)):
      sums[i] = sums[i-1] + self.w[i]
    rdm = randint(1, sums[-1])
    # print(f"{sums}, {rdm}")
    return bisect_left(sums, rdm)

  def pickIndex2(self):
      sums = list(itertools.accumulate(self.w))
      return bisect_left(sums, randint(1, sums[-1]))
#testing
for i in range(10):
  print(Solution([1,3]).pickIndex2())