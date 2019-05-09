"""
481 magical string
"""

def magicalString(n):
  s = "122"
  i = 2 # start from the index 2 count the number of next element and append it to the string
  while len(s) < n:
    s += int(s[i]) * str(int(s[-1]) ^ 3)
    i += 1
  return s[:n].count("1")

print(magicalString(1)) # 1
print(magicalString(6)) # 3