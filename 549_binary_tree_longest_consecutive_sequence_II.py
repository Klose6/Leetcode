"""
549 binary tree longest consecutive sequence II
"""
class Node:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

res = 0
def longest_consecutive(root):
  # return value is the longest increasing path and longest desceasing path start
  # from the current node
  if not root: return 0, 0
  left = longest_consecutive(root.left)
  right = longest_consecutive(root.right)
  cur_inc, cur_des = 1, 1
  if root.left:
    if root.val == root.left.val - 1:
      cur_inc = max(cur_inc, left[0]+1)
    elif root.val == root.left.val + 1:
      cur_des = max(cur_des, left[1]+1)
  if root.right:
    if root.val == root.right.val - 1:
      cur_inc = max(cur_inc, right[0] + 1)
    elif root.val == root.right.val + 1:
      cur_des = max(cur_des, right[1] + 1)
  global res
  # print(f"find: {root.val}, {left}, {right}")
  res = max(res, cur_inc + cur_des - 1)
  return cur_inc, cur_des


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n2.left = n1
n2.right = n3
n3.left = n4

longest_consecutive(n2)
print(res)