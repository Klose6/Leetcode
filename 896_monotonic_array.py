"""
896 monotonic array
"""


class Solution:
  def isMonotonic(self, A: List[int]) -> bool:
    return not {(i > j) - (i < j) for i, j in zip(A, A[1:])} >= {1, -1}
