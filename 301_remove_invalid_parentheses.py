"""
Remove all the invalid parentheses from a string and return the valid string
with minimum remove
"""
##1
def removeInvalidParentheses(s):
  result = []
  remove(s, result, 0, 0, ('(', ')'))
  return result

def remove(s, result, last_i, last_j, par):
  count = 0
  for i in range(last_i, len(s)):
    count += (s[i] == par[0]) - (s[i] == par[1])
    if count >= 0:
      continue
    for j in range(last_j, i + 1):
      if s[j] == par[1] and (j == last_j or s[j - 1] != par[1]):
        remove(s[:j] + s[j + 1:], result, i, j, par)
    return
  reversed_s = s[::-1]
  if par[0] == '(':
    remove(reversed_s, result, 0, 0, (')', '('))
  else:
    result.append(reversed_s)

##2 BFS
def remove_invalid_parentheses(s):
  if not s:
    return s
  def is_valid(v):
    count = 0
    for i in v:
      count += (i=="(") - (i==")")
      if count < 0:
        return False
    return count == 0
  level = [s]
  while True:
    next_level = filter(is_valid, level)
    if next_level:
      return list(set(next_level)) #remove the duplicated elements
    level = [v[:i]+v[i+1:] for v in level for i in range(len(v))]
    if not level:
      return level

input = "(a)())()"
print(remove_invalid_parentheses(input))


