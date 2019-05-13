"""
475 heaters
"""
from bisect import bisect_left

def findRadius(houses, heaters):
  res = float("-inf")
  heaters.sort()
  for h in houses:
    idx = bisect_left(heaters, h) # only need to find the insert point which is >= h
    left = abs(heaters[idx-1]-h) if idx-1 >= 0 else abs(heaters[0]-h)
    right = abs(heaters[idx]-h) if idx < len(heaters) else abs(heaters[-1]-h)
    # print(f"left: {left}, right: {right}")
    res = max(res, min(left, right))
  return res

print(findRadius([1,2,3], [2])) # 1
print(findRadius([1,2,3,4], [1,4])) # 2