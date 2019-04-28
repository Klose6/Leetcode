"""
526 beautiful arrangement
"""

def countArrangement(N):
  def count(i, X):
    if i == 1:
      return 1
    return sum(count(i-1, X-{x}) for x in X if x % i == 0 or i % x == 0)
  return count(N, set(range(1, N+1)))


def countArrangement2(N):
  cache = {}
  def helper(i, X):
    if i == 1:
      return 1
    key = (i, X) # use the current idx and values set as the cache key to save some time
    if key in cache:
      return cache[key]
    total = 0
    for j, v in enumerate(X): # try each value in the set for idx i
      if v % i == 0 or i % v == 0:
        total += helper(i-1, X[:j] + X[j+1:])
    cache[key] = total
    return total
  return helper(N, tuple(range(1, N+1)))

print(countArrangement2(2)) # 2