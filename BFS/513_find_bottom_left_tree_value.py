"""
Find bottom left tree value 513
"""
from sys import maxsize

max_dep = -maxsize
bottom_left_val = maxsize

def findBottomLeftVal(root, dep):
  global bottom_left_val, max_dep
  if not root:
    return
  if dep > max_dep:
    bottom_left_val = root.val
    max_dep = dep
  findBottomLeftVal(root.left, dep+1)
  findBottomLeftVal(root.right, dep+1)

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

root = Node(1)
root.left = Node(3)
root.right = Node(2)
findBottomLeftVal(root, 0)
print("Bottom Left Val: {}".format(bottom_left_val))
