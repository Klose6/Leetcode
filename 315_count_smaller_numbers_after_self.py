"""
315 count of smaller numbers after self
"""

class Node(object):
	def __init__(self, val):
		self.val = val
		self.left, self.right = None, None
		self.sum, self.dup = 0, 1

class Solution(object):
	def get_smaller(self, nums):
		if not nums:
			return
		def sort(enum):
			half = len(enum)/2
			if half:
				left, right = sort(enum[:half]), sort(enum[half:])
				for i in range(len(enum))[::-1]:
					if not right or left and left[-1][1] > right[-1][1]:
						smaller[left[-1][0]] += len(right)
						enum[i] = left.pop()
					else:
						enum[i] = right.pop()
			return enum
		smaller = [0]*len(nums)
		sort(list(enumerate(nums)))
		return smaller
	def get_smaller2(self, nums):
		if not nums:
			return
		res=[0]*len(nums)
		root=None
		for i,j in list(enumerate(nums))[::-1]:
			root=self.insert_bst(root, i, j, res, 0)
		return res
	def insert_bst(self, root, idx, i, res, presum):
		if not root:
			root=Node(i)
			res[idx]=presum
		elif i == root.val:
			root.dup += 1
			res[idx] = root.sum+presum
		elif i < root.val: #left
			root.sum += 1
			root.left = self.insert_bst(root.left, idx, i, res, presum)
		else: #right
			root.right = self.insert_bst(root.right, idx, i, res, root.sum+root.dup+presum)
		return root
s=Solution()
print s.get_smaller([5,2,6,1]) #[2,1,1,0]
print s.get_smaller2([5,2,6,1]) #[2,1,1,0]
