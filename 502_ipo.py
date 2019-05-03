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
  heap = []
  # sort the projects by their (caital, profit)
  projects = sorted(zip(capital, profits))
  i = 0
  for _ in range(k):
    # store all the projects that can be processed under the current capital
    while i < len(projects) and projects[i][0] <= W:
      heappush(heap, -projects[i][1]) # select the most profitable one
      i += 1
    if heap:
      W -= heappop(heap)
  return W

print(findMaxCapital(2, 0, [1,2,3], [0,1,1])) # 4