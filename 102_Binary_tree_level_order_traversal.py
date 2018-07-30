"""
102 Binary tree level order traversal
"""


class Node(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class Solution(object):
	def level_traversal(self, root):
		q = []
		res = []
		if not root: return res
		q.append(root)
		while q:
			level_num = len(q)
			tmp = []
			for _ in range(level_num):
				cur = q.pop(0)
				if cur.left: q.append(cur.left)
				if cur.right: q.append(cur.right)
				tmp.append(cur.val)
			res.append(tmp)
		return res


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n1.left = n2
n1.right = n3
print Solution().level_traversal(n1)
