"""
825 friends of appropriate ages
"""


class Solution:
  def numFriendRequests(self, ages: List[int]) -> int:
    res = 0
    start = 0
    dup = 1
    ages.sort()
    for i in range(len(ages)):
      if i > 0 and ages[i] == ages[i - 1]:
        dup += 1
      else:
        dup = 1
      if i < len(ages) - 1 and ages[i] == ages[i + 1]:
        continue
      while start < i and ages[start] <= 0.5 * ages[i] + 7:
        start += 1
      res += (i - start) * dup
    return res
