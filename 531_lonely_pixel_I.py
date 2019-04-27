"""
531 lonely pixel I
"""

def lonelyPixel(picture):
  if not picture: return 0
  m, n = len(picture), len(picture[0])
  rows, columns = [0]*m, [0]*n
  for i in range(m):
    for j in range(n):
      if picture[i][j] == "B":
        rows[i] += 1
        columns[j] += 1
  res = 0
  for i in range(m):
    for j in range(n):
      if picture[i][j] == "B" and rows[i] == 1 and columns[j] == 1:
        res += 1
  return res

print(lonelyPixel([
  ["W", "W", "B"],
  ["W", "B", "W"],
  ["B", "W", "W"],
]
)) # 3