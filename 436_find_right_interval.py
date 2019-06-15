"""
436 find right interval
"""

from bisect import bisect_left

def findRightInterval(intervals):
  if not intervals: return []
  tmp = sorted([(v[0], i) for i, v in enumerate(intervals)])
  res = []
  for i, v in enumerate(intervals):
    idx = bisect_left(tmp, (v[1], ))
    res.append(tmp[idx][1] if idx<len(tmp) else -1)
  return res

print(findRightInterval([[1,2]])) #[-1]
print(findRightInterval([[3,4],[2,3],[1,2]])) #[-1,0,1]