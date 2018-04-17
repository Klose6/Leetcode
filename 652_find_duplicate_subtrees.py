"""
652 find duplicate subtrees
"""
from collections import defaultdict


class Node(object):
	def __init__(self, v):
		self.val = v
		self.left = None
		self.right = None


class Solution(object):
	def find_dup_subtrees(self, root):
		# O(n*n)
		def trv(root):
			if not root:
				return "#"
			serial = str(root.val) + "," + trv(root.left) + "," + trv(root.right)
			map[serial].append(root)
			return serial

		map = defaultdict(list)
		trv(root)
		return [roots[0] for roots in map.values() if roots[1:]]

	def find_dup_subtrees2(self, root):
		# O(n*n)
		def tuplify(root):
			if root:
				tup = root.val, tuplify(root.left), tuplify(root.right)
				trees[tup].append(root)
				return tup

		trees = defaultdict(list)
		tuplify(root)
		return [roots[0] for roots in trees.values() if roots[1:]]

	def find_dup_subtrees3(self, root):
		# O(n)
		def getid(root):
			if root:
				id = treeid[root.val, getid(root.left), getid(root.right)]
				trees[id].append(root)
				return id

		trees = defaultdict(list)
		# Assign each new subtree a unique increased id
		treeid = defaultdict()
		treeid.default_factory = treeid.__len__
		getid(root)
		return [roots[0] for roots in trees.values() if roots[1:]]


n1 = Node(1)
n2 = Node(2)
n3 = Node(2)
n4, n5 = Node(4), Node(4)
n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
s = Solution()
print s.find_dup_subtrees(n1)
print s.find_dup_subtrees2(n1)
print s.find_dup_subtrees3(n1)
