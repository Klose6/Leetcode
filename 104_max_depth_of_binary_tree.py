"""
104 maximum depth of a binary tree
"""


def max_depth(root):
	if not root:
		return 0
	return 1 + max(max_depth(root.left), max_depth(root.right))
