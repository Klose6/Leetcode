"""
558 quad tree intersection
"""
class Node:
  def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
    self.val = val
    self.isLeaf = isLeaf
    self.topLeft = topLeft
    self.topRight = topRight
    self.bottomLeft = bottomLeft
    self.bottomRight = bottomRight

def quad_tree_intersection(q1, q2):
  if q1.isLeaf: #if q1 is leaf and it value is true, then we can directly return q1, otherwise we rely on q2
    return q1 if q1.val else q2
  elif q2.isLeaf:
    return q2 if q2.val else q1
  else:
    tLeft = quad_tree_intersection(q1.topLeft, q2.topLeft)
    tRight = quad_tree_intersection(q1.topRight, q2.topRight)
    bLeft = quad_tree_intersection(q1.bottomLeft, q2.bottomLeft)
    bRight = quad_tree_intersection(q1.bottomRight, q2.bottomRight)
    if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and \
        tLeft.val == tRight.val == bLeft.val == bRight.val:
      # if all the nodes are leaves and they have the same value
      node = Node(tLeft.val, True, None, None, None, None)
    else:
      node = Node(False, False, tLeft, tRight, bLeft, bRight)
  return node

