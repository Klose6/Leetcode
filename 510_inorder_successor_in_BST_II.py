"""
510 inorder successor in BST
"""

def findInorderSuccessor(root):
  """
  the inorder successor is either in its children nodes or in its parent nodes
  if its right child is not null, then the inorder successor is in its children nodes
  otherwise it should be in its parent nodes
  """
  if not root: return
  res = None
  if root.right:
    res = root.right
    while res and res.left:
      res = res.left
  elif root.parent:
    res = root.parent
    while res and res.val < root.val:
      res = res.parent
  return res