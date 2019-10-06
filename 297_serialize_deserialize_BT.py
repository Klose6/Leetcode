"""
297 serialize and deserialize a binary tree
"""
from utils import TreeNode

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


class Solution1:

	def serialize(self, root):
		if not root: return "#"
		return f"{root.val}{self.serialize(root.left)}{self.serialize(root.right)}"

	def deserialize(self, data):
		def helper(s):
			cur = next(s)
			if cur == "#": return
			node = TreeNode(cur)
			node.left = helper(s)
			node.right = helper(s)
			return node

		strs = iter(data)
		return helper(strs)
