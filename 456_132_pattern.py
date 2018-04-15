"""
456 132 Pattern
https://leetcode.com/problems/132-pattern/discuss/
"""
import sys

class Solution(object):
  def get_num_132_pattern(self, nums):
    if not nums:
      return False
    stack = []
    s3 = -sys.maxint - 1
    for i in range(len(nums))[::-1]:
      if nums[i] < s3:
        return True
      else:
        while stack and nums[i] > stack[-1]:
          s3 = stack[-1]
          stack.pop()
      stack.append(nums[i])
    return False

s = Solution()
print s.get_num_132_pattern([9,11,8,9,10,7,9])
print s.get_num_132_pattern([1,2,3])