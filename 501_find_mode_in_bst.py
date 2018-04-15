"""
find mode in binary search tree 501
https://leetcode.com/problems/find-mode-in-binary-search-tree/#/solutions
"""
class node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

def find_mode_bst(root):
  inorder(root)
  global res
  res = list()
  inorder(root)
  return res

def inorder(root):
  if not root:
    return
  inorder(root.left)
  handle_val(root.val)
  inorder(root.right)

cur_val = None
cur_count = 0
mode_count = 0
max_count = 0
cur_mode = None
res = None

def handle_val(val):
  global cur_val, max_count, cur_mode, mode_count, res
  if val != cur_val:
    cur_val = val
    cur_count = 0
  cur_count += 1
  if cur_count > max_count:
    max_count = cur_count
    cur_mode = val
  elif cur_count == max_count:
    if res != None:
      res.append(val)
    mode_count += 1

root = node(2)
root.left = node(1)
root.right = node(3)

find_mode_bst(root)
print(res)
