"""
101 symmetric tree
"""


class Solution(object):
	def is_symmetric(self, root):
		if not root:
			return True

		def is_equal(r1, r2):
			if not r1 or not r2:
				return r1 == r2
			if r1.val != r2.val:
				return False
			return is_equal(r1.left, r2.right) and is_equal(r1.right, r2.left)

		return is_equal(root.left, root.right)
