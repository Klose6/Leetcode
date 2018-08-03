"""
124 binary tree maximum path sum
"""
import sys


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


maxSum = -sys.maxint


def max_path_sum(root):
	max_path_down(root)
	return maxSum


def max_path_down(root):
	if not root:
		return 0
	left = max(0, max_path_down(root.left))
	right = max(0, max_path_down(root.right))
	global maxSum
	maxSum = max(maxSum, left + right + root.val)
	# the max path sum includes the current root
	return max(left, right) + root.val


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n1.left = n2
n1.right = n3
print max_path_sum(n1) == 6
