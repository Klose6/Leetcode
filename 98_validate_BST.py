"""
98 validate binary search tree
"""


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


class Solution(object):
	def validate_bst(self, root):
		if not root: return True
		stack = []
		pre = None
		while stack or root:
			while root:
				stack.append(root)
				root = root.left
			root = stack.pop()
			if pre and pre.val >= root.val: return False
			pre = root
			root = root.right
		return True

	def validate_bst2(self, root):
		def is_validate(root, minVal, maxVal):
			if not root: return True
			if not (minVal < root.val < maxVal): return False
			return is_validate(root.left, minVal, root.val) and \
						 is_validate(root.right, root.val, maxVal)

		return is_validate(root, float("-inf"), float("inf"))


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)
n2.left = n1
n2.right = n3
print Solution().validate_bst(n2) == True
print Solution().validate_bst2(n2) == True
