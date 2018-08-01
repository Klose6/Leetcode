"""
105 construct binary tree from preorder and inorder traversal
"""


class TreeNode(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None


def construct_bt(preorder, inorder):
	def helper(pre_start, in_start, in_end, preorder, inorder):
		if pre_start > len(preorder) - 1 or in_start > in_end:
			return None
		root = TreeNode(preorder[pre_start])
		index = 0
		for i in range(in_start, in_end + 1):
			if inorder[i] == root.val:
				index = i
				break
		root.left = helper(pre_start + 1, in_start, index - 1, preorder, inorder)
		root.right = helper(pre_start + index - in_start + 1, index + 1, in_end, preorder, inorder)

	return helper(0, 0, len(inorder) - 1, preorder, inorder)
