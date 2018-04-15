"""
459 repeated substring
https://leetcode.com/problems/repeated-substring-pattern/discuss/94334
"""

class Solution(object):
  def get_repeated_substring(self, s):
    if not s:
      return False
    t = s[1:] + s[:-1]
    return t.find(s) != -1

print Solution().get_repeated_substring("aaaa")
print Solution().get_repeated_substring("ababa")
