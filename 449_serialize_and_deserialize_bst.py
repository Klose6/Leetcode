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
      if vals and minVal < vals[0] < maxVal:
        val = deque.popleft()
        node = TreeNode(val)
        node.left = build(minVal, node.val)
        node.right = build(val, maxVal)
        return node
    return build(float("-inf"), float("inf"))
