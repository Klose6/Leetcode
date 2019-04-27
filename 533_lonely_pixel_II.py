"""
533 lonely pixel II

https://www.cnblogs.com/grandyang/p/6754987.html
"""
from collections import defaultdict

def lonely_pixel(picture, N):
  if not picture: return 0
  m, n = len(picture), len(picture[0])
  # print(f"{m}, {n}")
  rows_map = defaultdict(int) # store the whole row string to their frequencies mapping
  columns = [0] * n
  for i in range(m):
    count = 0
    for j in range(n):
      if picture[i][j] == "B":
        columns[j] += 1
        count += 1
    if count == N: # store the rows with N Bs
      rows_map["".join(picture[i])] += 1
  res = 0
  for k, v in rows_map.items(): # check the row strings
    if v == N:
      for i, c in enumerate(k): # check the columns count
        if c == "B" and columns[i] == N:
          res += N # add all the N rows
  return res

print(lonely_pixel([
  list("WBWBBW"), list("WBWBBW"), list("WBWBBW"), list("WWBWBW")
], 3)) # 6