"""
563 binary tree tilt
"""


def find_tilt(root):
  res = 0

  def node_sum(node):
    if not node:
      return 0
    left_sum = node_sum(node.left)
    right_sum = node_sum(node.right)
    res += abs(left_sum - right_sum)
    return left_sum + right_sum + node.val

  node_sum(root)
  return res
