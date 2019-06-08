"""
451 Sort characters by frequency
https://discuss.leetcode.com/topic/66045/c-o-n-solution-without-sort
https://discuss.leetcode.com/topic/66024/java-o-n-bucket-sort-solution-o-nlogn-priorityqueue-solution-easy-to-understand

"""
from collections import Counter
from heapq import heappush, heappop

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
    for key, val in freq.items():
      bucket[val].append(key)
    res = []
    # print bucket
    for i in range(l)[::-1]:
      if bucket[i]:
        res.append("".join([i * j for j in bucket[i]]))
    return "".join(res)

  def frequency_sort1(self, chars):
    if not chars: return ""
    count = Counter(chars)
    hq = [(c, v) for v, c in count.items()]
    # using a heapq to get the most frequent elements each time
    res = []
    for _ in range(len(hq)):
      c,v = heappop(hq)
      res.append(c*v)
    return "".join(res)

a = "AAzsz"
print(Solution().frequency_sort(a))
print(Solution().frequency_sort1(a))

