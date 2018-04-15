"""
Longest harmonious subsequence
"""
import collections

class Solution:
  def findLHS(self, nums):

    count = collections.Counter(nums)
    # for i in nums:
    #   count[i] += 1
    print(count)
    count = [count[i]+count[i+1] for i in count if count[i+1]] or [0]
    print(count)
    return max(count)

print(Solution().findLHS([1,3,2,2,5,2,3,7]))
print(Solution().findLHS([1,1,1]))
