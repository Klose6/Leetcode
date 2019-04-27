"""
530 minimum absolute difference in BST
"""
from sys import maxsize
from utils import TreeNode

res = maxsize
pre = None
def minDiff(root):
  # inorder visite the bst to get the min difference
  if not root: return
  minDiff(root.left)
  global res, pre
  if pre:
    res = min(res, root.val - pre)
  pre = root.val
  minDiff(root.right)

# if the tree if not a BST, then use the bisect to get the ceiling and floor for each element
from bisect import bisect_left, bisect_right
previous = []
res = maxsize

def minDiffBT(root):
  if not root: return
  minDiffBT(root.left)
  global res, previous
  if previous:
    floor = bisect_left(previous, root.val) # find the insert position
    print(f"val: {root.val}, floor: {floor}, previous: {previous}")
    if floor != len(previous): # if the insert position is within the index range
      res = min(res, abs(root.val - previous[floor]))
    else: # if the insert position pass the index range
      res = min(res, abs(root.val - previous[floor-1]))
    if floor + 1 < len(previous): # also check the potential bigger elements
      res = min(res, abs(previous[floor+1] - root.val))
    previous = previous[:floor] + [root.val] + previous[floor:] # insert the current element
  else:
    previous.append(root.val)
  print(f"min res: {res}")
  minDiffBT(root.right)

# testing
t1 = TreeNode(1)
t2 = TreeNode(3)
t3 = TreeNode(6)
t2.left = t3
t2.right = t1
minDiffBT(t2)
print(f"min diff in BT: {res}")