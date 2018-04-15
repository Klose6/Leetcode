"""
298 Binary tree longest consecutive sequences
http://www.cnblogs.com/grandyang/p/5252599.html
"""
class Node(object):
	def __init__(self, val):
		self.left, self.right = None, None
		self.val = val

class Solution(object):
	def get_longest_consecutive_seq(self, root):
		return self.helper(root, None, 0)
	def helper(self, root, par, curLen):
		if not root:
			return curLen
		curLen = curLen+1 if par and root.val == par.val + 1 else 1
		return max(self.helper(root.left, root, curLen),
										self.helper(root.right, root, curLen))


n1 = Node(1)
n2= Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n1.right=n3
n3.left=n2
n3.right=n4
n4.right=n5
s = Solution()
print s.get_longest_consecutive_seq(n1) # 3