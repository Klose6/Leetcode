"""
522 longest uncommon subsequence II
"""

def findLongestUncommon(strs):
  def isSubsequence(a, b):
    if len(a) > len(b): return False
    start = 0
    for i, v in enumerate(b):
      if start < len(a) and a[start] == v:
        start += 1
    return start == len(a)
  if not strs: return -1
  strs.sort(key=len, reverse=True)
  for i, s in enumerate(strs):
    if all(not isSubsequence(w, s) for j, w in enumerate(strs) if i != j):
      return len(s)
  return -1

print(findLongestUncommon(["aba", "cdc", "eae"])) # 3