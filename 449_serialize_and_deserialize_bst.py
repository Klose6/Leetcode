"""
449 serialize and deserialize BST
"""
from collections import deque
from utils import TreeNode

class Solution:

  def serialize(self, root):
    vals = []
    def preorder(root):
      if root:
        vals.append(root.val)
        preorder(root.left)
        preorder(root.right)
    preorder(root)
    return " ".join(map(str, vals))

  def deserialize(self, vals):
    # use deque instead of list, the performance is O(N)
    vals = deque([int(v) for v in vals.split()])
    def build(minVal, maxVal):
      if vals and minVal < vals[0] < maxVal: # use the minVal and maxVal to define the boundary in the vals
        val = deque.popleft()
        node = TreeNode(val)
        node.left = build(minVal, node.val)
        node.right = build(val, maxVal)
        return node
    return build(float("-inf"), float("inf"))

  def serialize1(self, root):
    vals = []
    def preorder(root):
      if not root:
        vals.append("#")
        return
      vals.append(str(root.val))
      preorder(root.left)
      preorder(root.right)
    preorder(root)
    return " ".join(vals)

  def deserialize1(self, vals):
    vals = iter(vals)
    def build():
      cur = next(vals.split())
      if cur == "#": return
      node = TreeNode(int(cur))
      node.left = build()
      node.right = build()
      return node
    return build()
