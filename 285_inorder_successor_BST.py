"""
285 inorder successor of a BST
"""


def inorder_successor(root, p):
	succ = None
	while root:
		if root.val > p.val:
			succ = root
			root = root.left
		else:
			root = root.right
	return succ
