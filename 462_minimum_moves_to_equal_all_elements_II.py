"""
462 minimum moves to equal array
"""

def minMoves(nums):
  if not nums or len(nums) < 2: return 0
  nums.sort()
  res = 0
  i, j = 0, len(nums)-1
  while i<j:
    res += nums[j] - nums[i]
    i += 1
    j -= 1
  return res

print(minMoves([1,2,3])) # 2