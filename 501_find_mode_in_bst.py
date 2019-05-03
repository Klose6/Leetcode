"""
find mode in binary search tree 501
https://leetcode.com/problems/find-mode-in-binary-search-tree/#/solutions
"""

from utils import TreeNode

class Solution:
  def findMode(self, root):
    self.mode_val = None
    self.mode_count = 0
    self.cur_val = None
    self.cur_count = 0
    self.res = []
    self.inorder(root)
    return self.res

  def inorder(self, node):
    if not node: return
    self.inorder(node.left)
    self.handle(node.val)
    self.inorder(node.right)

  def handle(self, val):
    if val != self.cur_val:
      self.cur_val = val
      self.cur_count = 0
    else:
      self.cur_count += 1
    if self.cur_count > self.mode_count:
      self.mode_count = self.cur_count
      self.mode_val = self.cur_val
      self.res = [self.cur_val]
    elif self.cur_count == self.mode_count:
      self.res.append(self.cur_val)
