"""
699 failing squares
https://discuss.leetcode.com/topic/107126/python-o-n-2-solution-with-explanation
https://leetcode.com/problems/falling-squares/solution/
"""

def getMaxHeights(heights):
  """
  heights: list[list[]]
  return:  list
  """
  if not heights:
    return []
  sq = [[heights[0][0], heights[0][1], heights[0][1]]]
  max_h = heights[0][1]
  res = [heights[0][1]]
  for point in heights[1:]:
    l = point[0]
    h = point[1]
    add = 0
    for prev in sq:
      if not l > prev[0]+prev[1] and not l+h < prev[0]:
        add = max(add, prev[2])
    sq.append([l, h, h+add])
    max_h = max(max_h, h+add)
    res.append(max_h)
  return res

print getMaxHeights([[1, 2], [2, 3], [6, 1]]) # [2,5,5]