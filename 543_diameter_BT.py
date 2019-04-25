"""
543 diameter of binary tree
"""
from utils import TreeNode


def diameterOfBinaryTreee(root):
  global res
  res = 0
  def depth(node):
    if not node: return 0
    left = depth(node.left)
    right = depth(node.right)
    global res
    res = max(res, left + right) # length of the longest path
    return max(left, right) + 1
  depth(root)
  return res


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.left = n2
n1.right = n3
n2.left = n4
print(diameterOfBinaryTreee(n1)) # 3