"""
587 erect the fence

https://leetcode.com/problems/erect-the-fence/discuss/103306/C++-and-Python-easy-wiki-solution
"""


class Solution(object):
	def erect_the_fence(self, points):
		def cross(o, a, b):
			return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

		if len(points) <= 1:
			return points
		points = sorted(points, key=lambda a: (a[0], a[1]))
		lower = []
		for p in points:
			if len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
				lower.pop()
			lower.append(p)
		upper = []
		for p in points[::-1]:
			if len(upper) >= 2 and cross(lower[-2], lower[-1], p) < 0:
				upper.pop()
			upper.append(p)
		res = []
		for r in lower[:-1] + upper[:-1]:
			if r not in res:
				res.append(r)
		return res


print Solution().erect_the_fence([[1, 2], [2, 2], [4, 2]]) == [[1, 2], [2, 2], [4, 2]]
