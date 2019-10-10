"""
958 check completeness of a binary tree
"""


class Solution:
  def isCompleteTree(self, root: TreeNode) -> bool:
    if not root: return True
    bfs = [root]
    i = 0
    while bfs[i]:
      bfs.append(bfs[i].left)
      bfs.append(bfs[i].right)
      i += 1
    return not any(bfs[i:])
