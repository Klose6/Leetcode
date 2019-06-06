"""
453 Minimum moves to equal array elements
https://discuss.leetcode.com/topic/66737/it-is-a-math-question

the min number in the arrays has to move for all the moves
"""


class Solution(object):
  def min_moves(self, nums):
    if not nums:
      return 0
    return sum(nums)-len(nums)*min(nums)

print(Solution().min_moves([1,2,3])) # 3