
"""161 one edit distance"""
class Solution:
  def isOneEditDistance(self, s: str, t: str) -> bool:
    lens, lent = len(s), len(t)
    for i in range(min(lens, lent)):
      if s[i] != t[i]:
        if lens == lent:  # replace
          return s[i + 1:] == t[i + 1:]
        elif lens > lent:  # delete one from s
          return s[i + 1:] == t[i:]
        else:  # insert one into s
          return s[i:] == t[i + 1:]
    return abs(lens - lent) == 1