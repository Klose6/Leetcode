"""
545 boundary of binary tree
"""

def leftBoundary(root ,nodes):
  if not root or (not root.left and not root.right):
    return
  nodes.append(root)
  # always check the left side to find the non-leave node
  if not root.left:
    leftBoundary(root.right, nodes)
  else:
    leftBoundary(root.left, nodes)

def rightBoundary(root, nodes):
  if not root or (not root.left and not root.right):
    return
  nodes.append(root)
  # always check the right side to find the non-leave node
  if not root.right:
    rightBoundary(root.left, nodes)
  else:
    rightBoundary(root.right, nodes)

def leaves(root, nodes):
  if not root: return
  if not root.left and not root.right:
    nodes.append(root)
    return
  leaves(root.left, nodes)
  leaves(root.right, nodes)

def boundaryOfBinaryTree(root):
  if not root: return []
  nodes = [root]
  leftBoundary(root.left, nodes)
  rightBoundary(root.right, nodes)
  leftBoundary(root, nodes)
  return nodes

def boundaryOfBinaryTree_2(root):
  if not root: return []
  nodes = [root]
  left, node, right = root.left, root, root.right
  # get the left boundary
  while left and (left.left or left.right):
    nodes.append(left)
    if left.left:
       left = left.left
    else:
      left = left.right
  # get the leaves using preorder traverse
  st = []
  while node or st:
    if node:
      st.append(node)
      if not node.left and not node.right:
        nodes.append(node)
      node = node.left
    else:
      node = st.pop()
      node = node.right
  # get the right boundary
  rights = []
  while right and (right.left or right.right):
    rights.append(right)
    if right.right:
      right = right.right
    else:
      right = right.left
  nodes.extend(rights[::-1])
  return nodes

# testing
from utils import TreeNode
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n4 = TreeNode(4)
n1.right = n2
n2.left = n3
n2.right = n4
nodes = boundaryOfBinaryTree_2(n1)
print(f"{[n.val for n in nodes]}")