"""
559 maximum depth of n-ary tree
"""


def find_max_depth(root):
  if not root: return 0
  if not root.children: return 1
  return max([find_max_depth(child) for child in root.children]) + 1


def find_max_depth1(root):
  if not root: return 0
  q = [root]
  depth = 0
  while q:
    size = len(q)
    for i in range(size):
      cur = q.pop(0)
      q.extend([child for child in cur.children])
    depth += 1
  return depth
