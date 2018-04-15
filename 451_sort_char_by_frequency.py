"""
451 Sort characters by frequency
https://discuss.leetcode.com/topic/66045/c-o-n-solution-without-sort
https://discuss.leetcode.com/topic/66024/java-o-n-bucket-sort-solution-o-nlogn-priorityqueue-solution-easy-to-understand

"""
from collections import Counter
class Solution:
  def __init__(self):
    pass

  def frequency_sort(self, chars):
    if not chars:
      return chars
    # compute the frequency
    freq = Counter(chars)
    l = len(chars)
    # bucket sort
    bucket = [[] for _ in range(l)]
    for key, val in freq.iteritems():
      bucket[val].append(key)
    res = []
    # print bucket
    for i in range(l)[::-1]:
      if bucket[i]:
        res.append("".join([i * j for j in bucket[i]]))
    return "".join(res)

a = "AAzsz"
print Solution().frequency_sort(a)

