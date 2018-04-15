"""
IPO 502
https://discuss.leetcode.com/topic/77768/very-simple-greedy-java-solution-using-two-priorityqueues
https://discuss.leetcode.com/topic/77795/python-solution
pyhton heapq:
https://github.com/qiwsir/algorithm/blob/master/heapq.md
"""
from queue import PriorityQueue as pq
from heapq import *

def findMaxCapital(k, W, profits, capital):
  cur = []
  future = sorted(zip(capital, profits))[::-1]
  for _ in range(k):
    while future and future[-1][0] <= W:
      heappush(cur, -future.pop()[1])
    if cur:
      W -= heappop(cur)
  return W

print(findMaxCapital(2, 0, [1,2,3], [0,1,1]))