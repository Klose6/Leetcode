"""
452 Minimum number of arrows to burst balloons
https://discuss.leetcode.com/topic/73981/share-my-explained-greedy-solution-as-the-highest-voted-java-solution-right-now-is-not-ideal
https://discuss.leetcode.com/topic/66772/greedy-python-132-ms
"""
import copy

class Solution:
  def __init__(self):
    pass
  def min_num(self, points):
    if not points:
      return 0
    dup = sorted(points, key=lambda x: x[1])
    start, end = 0, -float("inf")
    # print start, end
    res = 0
    # print dup
    for i in dup:
      if i[0] > end:
        res += 1
        end = i[1]
    return res

print(Solution().min_num([[10,16],[2,8],[1,6],[7,12]])) #2