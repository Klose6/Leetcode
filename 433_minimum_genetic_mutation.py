"""
433 minimum genetic mutation
https://leetcode.com/problems/minimum-genetic-mutation/discuss/91489/Python-Solution-using-BFS
"""
from collections import deque


def variableMutation(cur, next):
  changes = 0
  for i in range(len(cur)):
    if cur[i] != next[i]:
      changes += 1
  return changes

def getMinMutation(start, end, bank):
  if start == end: return 0
  count = 0
  visited = {start}
  bankset = set(bank) # use a set to speed the check-in op
  q = deque() # use a deque so that the pop is O(1)
  q.append(start)
  while q:
    for _ in range(len(q)):
      cur = q.popleft()
      if cur == end: return count
      for c in range(len(cur)):
        for i in ('A', 'C', 'G', 'T'):
          if i == cur[c]: continue # avoid create the same str
          mut = cur[:c] + i + cur[c+1:]
          if mut in visited or mut not in bankset:
            continue
          q.append(mut)
    count += 1
  return -1

print(getMinMutation("AACCGGTT", "AACCGGTA", ["AACCGGTA"])) # 1