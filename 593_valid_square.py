"""
Valid square
"""

class Solution:
  """
  consider the four edges, should only have two non-zero and distinct values.
  """
  def validSquare(self, p1, p2, p3, p4):
    len_set = set()
    ps = [p1, p2, p3, p4]
    for i in range(len(ps)):
      for j in range(i+1, len(ps)):
        len_set.add(self.dis(ps[i], ps[j]))

    return 0 not in len_set and len(len_set) == 2

  def dis(self, a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


print(Solution().validSquare([0, 0], [1, 1], [1, 0], [0, 1]))
print(Solution().validSquare([0, -1], [1, 1], [1, 0], [0, 1]))
