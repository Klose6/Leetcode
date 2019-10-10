"""
973 k closest points to origin
"""
from heapq import heappush, heappop


class Solution:
  def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
    if not points: return []
    heap = []
    for p in points:
      heappush(heap, (-(p[0] ** 2 + p[1] ** 2), p))
      if len(heap) > K:
        heappop(heap)
    return [i[1] for i in heap]
