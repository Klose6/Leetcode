"""
477 total hamming distance
"""

def findTotalDistance(nums):
  if not nums: return 0
  res = 0
  for i in range(32):
    count = 0
    for j in nums: # for each bit, find the #1s and #0s, then the add the total to res, which is #1s*#0s
      if 1 & (j >> i) == 1:
        count += 1
    res += count * (len(nums) - count)
  return res