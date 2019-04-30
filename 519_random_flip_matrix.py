"""
519 random flip matrix

Using the Fisher-Yates shuffle to generate a list of random numbers
the steps are:
1.generate the random number from 0 to n: m
2 swap m and n
3. decrease the n
"""
import random

class Solution:
  def __init__(self, rows, columns):
    self.rows = rows
    self.columns = columns
    self.total = self.rows * self.columns - 1
    self.map = {} # save the random idx so that we can reuse them later

  def flip(self):
    # generate the index
    r = random.randint(0, self.total)
    # check if we have already have something at this index
    x = self.map.get(r, r)
    # swap - so the next time we will not use the previous index and also according to the algorithm
    self.map[r] = self.map.get(self.total, self.total)
    self.total -= 1
    return [x // self.columns, x % self.columns]

  def reset(self):
    self.map.clear()
    self.total = self.rows * self.columns - 1

#testing
s = Solution(2,3)
for i in range(4):
  print(f"{s.flip()}")