"""
536 construct binary tree from string
"""
from utils import TreeNode

def constructBT(s):
  if not s: return None
  # print(f"s: {s}")
  paren = s.find("(")
  val = int(s) if paren == -1 else int(s[:paren])
  node = TreeNode(val)
  if paren == -1: return node # if no parentheses found, then return
  start, count = paren, 0
  for i in range(start, len(s)):
    if s[i] == "(": count += 1
    elif s[i] == ")": count -= 1
    if count == 0 and start == paren: # build the left child
      node.left = constructBT(s[start+1:i])
      start = i+1 # start process the right child's string
    elif count == 0: # build the right child
      node.right = constructBT(s[start+1:i])
  return node

root = constructBT("4(2(3)(1))(6(5))")
print(f"root: {root.val}, left: {root.left.val}, right: {root.right.val}")