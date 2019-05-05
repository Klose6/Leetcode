"""
491 increasing subsequences
"""

def findSubsequences(nums):
  if not nums: return []
  res = set() # use set since it will be faster than list when check the value in it or not
  for n in nums:
    tmp = {(n,)}
    for r in res:
      if r[-1] <= n:
        tmp.add(r+(n,))
    for t in tmp:
      if t not in res:
        res.add(t)
  return [list(r) for r in res if len(r) > 1]

print(findSubsequences([4,6,7,7]))