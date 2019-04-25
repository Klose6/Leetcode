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