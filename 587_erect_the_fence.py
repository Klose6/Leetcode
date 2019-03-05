"""
587 erect the fence

https://www.algorithmist.com/index.php/Monotone_Chain_Convex_Hull.py
"""


class Solution(object):
	def erect_the_fence(self, points):
    # 2D cross product of OA and OB, return positive if the product is counter-clockwise turn
    # return negative if the product if clockwise turn
		def cross(o, a, b):
			return (b[1] - o[1]) * (a[0] - o[0]) - (a[1] - o[1]) * (b[0] - o[0])

		if len(points) <= 1:
			return points
    # sort the point list from lower to high
		points = sorted(points, key=lambda a: (a[0], a[1]))
    # get the lower hull
		lower = []
		for p in points:
			if len(lower) >= 2 and cross(lower[-2], lower[-1], p) < 0:
				lower.pop()
			lower.append(p)
    # get the upper hull
		upper = []
		for p in points[::-1]:
			if len(upper) >= 2 and cross(lower[-2], lower[-1], p) < 0:
				upper.pop()
			upper.append(p)
    # return the unique point list
		res = []
		for r in lower[:-1] + upper[:-1]:
			if r not in res:
				res.append(r)
		return res


assert Solution().erect_the_fence([[1, 2], [2, 2], [4, 2]]) == [[1, 2], [2, 2], [4, 2]]
