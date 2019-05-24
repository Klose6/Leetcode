"""
466 count the repetitions
"""

def countRepetitions(s1, n1, s2, n2):
  """
  use the brute force way
  """
  count1, count2 = 0, 0
  i, j = 0, 0
  while count1 < n1:
    if s1[i] == s2[j]:
      j += 1
      if j == len(s2):
        j = 0
        count2 += 1
    i += 1
    if i == len(s1):
      i = 0
      count1 += 1
  return count2 // n2

print(countRepetitions("acb", 4, "ab", 2)) # 2
