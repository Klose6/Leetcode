"""
524 longest wod in dictionary through deleting
"""

def findLongestWord(s, d):
  def match(s, t):
    if len(s) < len(t): return False
    start = 0
    for i, v in enumerate(s):
      if start < len(t) and v == t[start]:
        start += 1
    return start == len(t)
  matches = [w for w in d if match(s, w)]
  return sorted(matches, key=lambda x: (-len(x), x))[0] if matches else []

def findLongestWord2(s, d):
  def match(s, t):
    if len(s) < len(t): return False
    start = 0
    for i, v in enumerate(s):
      if start < len(t) and v == t[start]:
        start += 1
    return start == len(t)
  res = ""
  for w in d:
    if match(s, w) and (len(w) > len(res) or w < res):
      res = w
  return res

# testing
print(findLongestWord("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(findLongestWord("abpcplea", ["a", "b", "c"]))

print(findLongestWord2("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(findLongestWord2("abpcplea", ["a", "b", "c"]))