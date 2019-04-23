"""
555 split concatenated strings
"""

def splitLoopedStrings(strs):
  if not strs: return ""
  s = "".join([max(s, s[::-1]) for s in strs])
  res, start = "a", 0
  # print(s)
  for i, st in enumerate(strs): # construct the str starts with the current cut
    body = s[start + len(st):] + s[:start]
    for p in st, st[::-1]: # the current str can be original or reverse
      for j in range(len(st)):
        if p[j] >= res[0]:
          res = max(res, "".join([p[j:], body, p[:j]]))
    start += len(st)
  return res

print(splitLoopedStrings(["abc", "xyz"]))

