"""
532 k-diff pairs in an array
"""
from collections import Counter

def kDiffPairs(nums, k):
  if not nums: return 0
  c = Counter(nums)
  res = 0
  for v in sorted(c.keys()):
    if k == 0: # deal with the special case k == 0
      if c[v] >= 2:
        res += 1
    elif v + k in c:
      res += 1
  return res

print(kDiffPairs([3,1,4,1,5], 2)) # 2
print(kDiffPairs([1,3,4,1,5], 0)) # 1