"""
94 binary tree inorder traversal
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def bst_inorder(root):
	res = []
	if not root:
		return
	stack = []
	cur = root
	while cur or stack:
		while cur:
			stack.append(cur)
			cur = cur.left
		node = stack.pop()
		res.append(node.val)
		cur = node.right
	return res


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.right = n2
n2.left = n3
print bst_inorder(n1)
