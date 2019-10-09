"""
986 interval list intersections
"""


class Solution:
  def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    if not A or not B: return []
    res = []
    i, j = 0, 0
    m, n = len(A), len(B)
    while i < m and j < n:
      if A[i][0] > B[j][1]:
        j += 1
      elif A[i][1] < B[j][0]:
        i += 1
      else:
        res.append((max(A[i][0], B[j][0]), min(A[i][1], B[j][1])))
        if A[i][1] <= B[j][1]:
          i += 1
        else:
          j += 1
    return res
