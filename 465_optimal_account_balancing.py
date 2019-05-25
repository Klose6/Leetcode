"""
465 optimal account balancing
https://www.cnblogs.com/grandyang/p/6108158.html
"""

from collections import defaultdict

def minTransfers(transactions):
  if not transactions:
    return 0
  m = defaultdict(int)
  for t in transactions:
    m[t[0]] -= t[2]
    m[t[1]] += t[2]
  account = [v for i, v in m.items() if v != 0]
  return dfs(account, 0, 0)

def dfs(account, start, num):
  res = float("inf")
  while start < len(account) and account[start] == 0: start += 1
  for i in range(start+1, len(account)):
    if account[i] < 0 and account[start] > 0 or \
      account[i] > 0 and account[start] < 0:
      account[i] += account[start]
      res = min(res, dfs(account, start+1, num+1))
      account[i] -= account[start]
  return num if res == float("inf") else res

print(minTransfers([[0,1,10], [2,0,5]])) # 2
print(minTransfers([[0,1,10], [1,0,1], [1,2,5], [2,0,5]])) # 1