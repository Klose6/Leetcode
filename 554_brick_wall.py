"""
554 brick wall
"""
from collections import defaultdict

def least_bricks(wall):
  """
  walls(list[list[int]]):
  """
  if not wall: return 0
  # find the total number of columns
  max_len = max([sum(w) for w in wall])
  res = [0] * max_len
  print(f"max_len: {max_len}")
  for w in wall:
    start = 0
    for i in w:
      res[start] += 1 # mark the start of each bricks
      # res[start+i-1] += 1
      start += i
    print(f"res: {res}")
  return len(wall) - max(res[1:-1]) # find the most common brick edge and use it as the cut

def least_bricks_2(wall):
  if not wall: return 0
  points = defaultdict(int)
  count = 0
  for w in wall:
    start = 0
    for i in w[:-1]: # use the end of each brick to count, also need to skip the last brick
      start += i
      points[start] += 1
      count = max(count, points[start])
  print(f"points: {points}")
  return len(wall) - count

wall = [
  [1,2,2,1],
  [3,1,2],
  [1,3,2],
  [2,4],
  [3,1,2],
  [1,3,1,1]
]
# testing
# print(least_bricks(wall)) # 2
print(least_bricks_2(wall)) # 2