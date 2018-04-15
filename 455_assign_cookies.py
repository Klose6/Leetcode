"""
455 Assign Cookies
https://discuss.leetcode.com/topic/67676/simple-greedy-java-solution
https://discuss.leetcode.com/topic/68147/simple-python-o-nlogn
"""

class Solution(object):
  def assign_cookies(self, g, s):
    """
    Args:
      g(list): the greed factors of all the children
      s(list): the cookie size list you have
    Returns:
      int: the max num of children to gratify
    """
    if not g or not s:
      return 0
    g.sort()
    s.sort()
    i, j = 0, 0
    while i < len(g) and j < len(s):
      if g[i] <= s[j]:
        i += 1
      j += 1
    return i

print Solution().assign_cookies([1,2,3], [1,1])