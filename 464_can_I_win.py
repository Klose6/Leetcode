"""
464 can I win
"""

def canWin(maxChoosableInteger, desiredTotal):
  sum = maxChoosableInteger * (maxChoosableInteger + 1) // 2
  if sum < desiredTotal:
    return False
  if desiredTotal <= 0:
    return True
  used = [0] * (maxChoosableInteger + 1)
  used[0] = 1
  return dfs(used, desiredTotal)

cache = {}

def dfs(used, desiredTotal):
  if desiredTotal <= 0: return False
  k = int("".join(map(str, used)))
  if k in cache: return cache[k]
  for i, v in enumerate(used):
    if v == 0:
      used[i] = 1
      if not dfs(used, desiredTotal - i):
        cache[int("".join(map(str, used)))] = True
        used[i] = 0
        return True
      used[i] = 0
  cache[k] = False
  return False

print(canWin(10, 11)) # False
print(canWin(10, 40)) # False