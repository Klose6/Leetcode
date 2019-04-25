"""
541 reverse string II
"""

def reverseString(s, k):
  if not s : return s
  sl = list(s)
  for i in range(0, len(sl), 2*k):
    sl[i: i+k] = reversed(sl[i: i+k])
  return "".join(sl)

print(reverseString("abcdefg", 2))