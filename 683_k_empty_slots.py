"""
683 K empty slots
http://bookshadow.com/weblog/2017/09/24/leetcode-k-empty-slots/
https://www.cnblogs.com/grandyang/p/8415880.html
"""
import bisect
import sys

class Solution:
	def get_k_empty_slots(self, flowers, k):
		"""
		transfer the flowers array to an days array to indicate the day that flower[i] will blooming
		O(n), O(n)
		"""
		if not flowers:
			return -1
		n = len(flowers)
		days = [0] * n
		for i, f in enumerate(flowers):
			days[f-1] = i+1
		res = sys.maxint
		left, right = 0, k+1
		for i in xrange(n):
			if right >= n:
				break
			if days[i] < days[left] or days[i] <= days[right]:
				if i == right:
					res = min(res, max(days[left], days[right]))
				left, right = i, i+k+1
		return -1 if res == sys.maxint else res

	def get_k_empty_slots_2(self, flowers, k):
		"""
		using Fenwick tree to check each element
		O(nlogn), O(nlogn)
		"""
		maxn = max(flowers)
		bloomed = [0] * (maxn+1)
		ft = FenwickTree(maxn)
		for i, v in enumerate(flowers):
			ft.add(v, 1)
			bloomed[v] = 1
			if v >= k and ft.sum(v) - ft.sum(v-k-2) == 2 and bloomed[v-k-1]:
				return i+1
			if v+k+1 <= maxn and ft.sum(v+k+1) - ft.sum(v-1) == 2 and bloomed[v+k+1]:
				return i+1
		return -1

class FenwickTree(object):
	"""
	using Fenwick Tree to check each days -k backward and +k forward
	"""
	def __init__(self, n):
		self.n = n
		self.sums = [0] * (n+1)
	def add(self, x, val):
		while x <= self.n:
			self.sums[x] += val
			x += self.lowbit(x)
	def lowbit(self, x):
		return x & -x
	def sum(self, x):
		res = 0
		while x > 0:
			res += self.sums[x]
			x -= self.lowbit(x)
		return res

s = Solution()
# solution 1
print s.get_k_empty_slots([1,3,2], 1) #2
print s.get_k_empty_slots([1,2,3], 1) #-1
# solution 2
print s.get_k_empty_slots_2([1,3,2], 1) #2
print s.get_k_empty_slots_2([1,2,3], 1) #-1