"""
Squirrel simulation
"""


def getMinDistance(squirrel, nuts, tree):
  """
  the distance from tree to all the nuts is fix, we needs to find the min distance
  from the squirrel to the first-to-pick nut, for each round we have two choices: pick or not,
  if pick then the distance is x + y(assume squirrel to nut is y and nut to tree is x),
  otherwise is x + x, we want to find the min x+y, which is find the min result distance
  """
  res = 0
  max_diff = 0
  for n in nuts:
    dis = abs(n[0] - tree[0]) + abs(n[1] - tree[1])
    res += 2 * dis
    max_diff = max(max_diff, dis - abs(n[0] - squirrel[0]) - abs(n[1] - squirrel[1]))
  return res - max_diff


print(getMinDistance([4, 4], [[3, 0], [2, 5]], [2, 2]))
