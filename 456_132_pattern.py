"""
456 132 Pattern
https://leetcode.com/problems/132-pattern/discuss/
"""

class Solution(object):
  def get_num_132_pattern(self, nums):
    if not nums:
      return False
    stack = []
    s3 = float("-inf")
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
print(s.get_num_132_pattern([3,1,4,2])) # True
print(s.get_num_132_pattern([1,2,3])) # False