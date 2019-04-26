"""
538 convert bst to greater tree
"""
from utils import TreeNode

sum = 0
def convertBST(root):
  # traverse from right node -> current node -> left node
  if not root: return
  convertBST(root.right)
  global sum
  sum += root.val
  print(f"{root.val} -> {sum}")
  root.val = sum
  convertBST(root.left)

t1 = TreeNode(5)
t2 = TreeNode(2)
t3 = TreeNode(13)
t4 = TreeNode(10)
t1.left = t2
t1.right = t3
t3.left = t4
convertBST(t1)