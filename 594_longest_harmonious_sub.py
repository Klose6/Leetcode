"""
Longest harmonious sub-sequences
"""
import collections

class Solution:
  def findLHS(self, nums):
    count = collections.Counter(nums)
    res = 0
    for i in count:
      if i + 1 in count:
        res = max(res, count[i] + count[i + 1])
    return res
    # count = [count[i]+count[i+1] for i in count if count[i+1]] or [0]
    # return max(count)

print(Solution().findLHS([1,3,2,2,5,2,3,7]))
print(Solution().findLHS([1,1,1]))
