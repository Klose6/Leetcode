"""
454 4Sum II
https://discuss.leetcode.com/topic/67593/clean-java-solution-o-n-2
https://discuss.leetcode.com/topic/67659/easy-2-lines-o-n-2-python
"""
from collections import Counter

class Solution(object):
  def four_sum_count(self, A, B, C, D):
    if not A or not B or not C or not D:
      return 0
    AB = Counter([a+b for a in A for b in B])
    return sum(AB[-c-d] for c in C for d in D)

print Solution().four_sum_count([1,2],[-2,-1],[-1,2],[0,2])