"""
Find largest value in each tree row 515
https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/
https://discuss.leetcode.com/topic/78991/python-bfs
"""
from utils import TreeNode
from queue import Queue
from sys import maxsize

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def findLargestInTreeRow(root):
  q = [root]
  maxes = []
  while q:
    maxes.append(max(node.val for node in q))
    q = [c for node in q for c in (node.left, node.right) if c]
  return maxes

result = []
def dfs(root, dep):
  if not root:
    return
  if dep == len(result):
    result.append(root.val)
  else:
    result[dep] = max(result[dep], root.val)
  dfs(root.left, dep+1)
  dfs(root.right, dep+1)
  return result

#testing
root = Node(1)
root.left = Node(3)
root.right = Node(2)

print(findLargestInTreeRow(root))
print(dfs(root, 0))