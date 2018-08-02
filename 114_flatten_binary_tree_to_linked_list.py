"""
114 flatten binary tree to linked list
"""


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


prev = None


def flatten(root):
	if not root:
		return
	flatten(root.right)
	flatten(root.left)
	global prev
	root.right = prev
	root.left = None
	prev = root


def flatten1(root):
	cur = root
	while cur:
		if cur.left:
			pre = cur.left
			while pre.right:
				pre = pre.right
			pre.right = cur.right
			cur.right = cur.left
			cur.left = None
		cur = cur.right
