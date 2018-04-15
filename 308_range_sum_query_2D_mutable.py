"""
Range sum query 2D mutable
http://www.cnblogs.com/grandyang/p/5300458.html
http://www.cnblogs.com/yrbbest/p/5058571.html
"""

class Solution(object):
	"""
	Binary index tree - 2D version
	"""
	def __init__(self, m):
		if not m:
			return
		self.bit = [[0]*(len(m[0])+1) for _ in range(len(m)+1)]
		# copy of the original matrix for update
		self.m = [[0]*len(m[0]) for _ in range(len(m))]
		i, j = 0, 0
		p, q = len(self.m), len(self.m[0])
		while i < p:
			j=0
			while j < q:
				self.update(i, j, m[i][j])
				j += 1
			i += 1
	def update(self, r, c, v):
		diff = v - self.m[r][c]
		i, j = r+1, c+1
		p, q = len(self.bit), len(self.bit[0])
		while i < p:
			j = c+1
			while j < q:
				self.bit[i][j] += diff
				j += j&-j
			i += i&-i
		self.m[r][c] = v
	def get_sum(self, r, c):
		sum = 0
		i, j = r, c
		while i > 0:
			j = c
			while j > 0:
				sum += self.bit[i][j]
				j -= j&-j
			i -= i&-i
		print r, c, sum
		return sum
	def range_sum(self, r1, c1, r2, c2):
		if not self.m:
			return
		return self.get_sum(r2+1, c2+1) - self.get_sum(r1, c2+1) - \
		self.get_sum(r2+1, c1) + self.get_sum(r1, c1)

ms = "30142\n56321\n12015\n41017\n10305"
m = [[int(i) for i in j] for j in ms.splitlines()]
print m
s = Solution(m)
print s.m
print s.range_sum(2,1,4,3) #8
s.update(3,2,2)
print s.m
print s.range_sum(2,1,4,3) #10

