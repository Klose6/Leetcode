"""
572 subtree of another tree
"""


class Node:
  def __init__(self, val):
    self.val = val
    self.left = self.right = None


def isSubtree(t1, t2):
  if isSameTree(t1, t2):
    return True
  if not t1:
    return False
  return isSubtree(t1.left, t2) or isSubtree(t1.right, t2)


def isSameTree(a, b):
  if not a or not b:
    return a is b
  return a.val == b.val and isSameTree(a.left, b.left) and isSameTree(a.right, b.right)


# store the hash of the current tree to the current node
from hashlib import sha256


def getHash(s):
  S = sha256()
  S.update(s)
  return S.hexdigest()


def isSubtree2(t1, t2):
  def merkle(node):
    if not node:
      return "#"
    m_left = merkle(node.left)
    m_right = merkle(node.right)
    node.merkle = getHash(m_left + str(node.val) + m_right)

  # process the tree the compute all the ubstree hashes
  merkle(t1)
  merkle(t2)

  # dfs the tree the find whether there is a subtree
  def dfs(node):
    if not node:
      return False
    return node.merkle == t2.merkle or dfs(node.left) or dfs(node.right)

  return dfs(t1)
