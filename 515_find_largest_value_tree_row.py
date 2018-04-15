"""
Find largest value in each tree row 515
https://leetcode.com/problems/find-largest-value-in-each-tree-row/discuss/
https://discuss.leetcode.com/topic/78991/python-bfs
"""
from queue import Queue
from sys import maxsize

class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def findLargestInTreeRow(root):
  res = []
  q = Queue()
  q.put(root)
  q.put(None)
  cur_max = -maxsize
  while not q.empty():
    cur = q.get()
    if not cur:
      res.append(cur_max)
      if not q.qsize():
        return res
      q.put(None)
      cur_max = -maxsize
      continue
    cur_max = max(cur_max, cur.val)
    if cur.left:
      q.put(cur.left)
    if cur.right:
      q.put(cur.right)
  return res

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
root = Node(1)
root.left = Node(3)
root.right = Node(2)

print(findLargestInTreeRow(root))
print(dfs(root, 0))