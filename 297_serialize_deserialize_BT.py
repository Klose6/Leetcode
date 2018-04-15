"""
297 serialize and deserialize a binary tree
"""
class Node(object):
	def __init__(self, val):
		self.val = val
		self.left, self.rgiht= None,None

class Solution(object):
	def serialize(self, root):
		def helper(root):
			if not root:
				res.append("#")
				return
			res.append(root.val)
			helper(root.left)
			helper(root.right)
		res= []
		helper(root)
		return " ".join(res)
	def deserialize(self, s):
		def helper():
			cur = next(res)
			if s == "#":
				return None
			root = Node(cur)
			root.left = helper()
			root.right = helper()
			return root
		res = iter(s.split())
		return helper()