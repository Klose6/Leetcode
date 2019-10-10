"""
1027 longest arithmetic sequence
"""

from collections import defaultdict


class Solution:
  def longestArithSeqLength(self, A: List[int]) -> int:
    if not A: return 0
    d = defaultdict(dict)
    res = 2
    for i in range(len(A)):
      d[i] = defaultdict(int)
      for j in range(i):
        diff = A[i] - A[j]
        d[i][diff] = d[j].get(diff, 1) + 1
        res = max(res, d[i][diff])
    return res
