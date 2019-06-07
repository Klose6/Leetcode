"""
Delete node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/discuss/
https://leetcode.com/problems/delete-node-in-a-bst/discuss/93296/Recursive-Easy-to-Understand-Java-Solution
"""


class Node(object):
  def __init__(self, x):
    self._val = x
    self.left = None
    self.right = None

class Solution(object):
  def delete_node_bst(self, root, key):
    if not root:
      return
    if root.val < key:
      root.left = self.delete_node_bst(root.left, key)
    elif root.val > key:
      root.right = self.delete_node_bst(root.right, key)
    else: # the key == root.val
      if not root.left:
        return root.right
      elif not root.right:
        return root.left
      # both the left and right child exist
      min_node = self.find_min(root.right)
      root.val = min_node.val # assign the min value in the right tree to the root
      root.right = self.delete_node_bst(root.right, root.val) # go through the smallest path to remove the min node
    return root

  def find_min(self, node):
    while node.left:
      node = node.left
    return node
