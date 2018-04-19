"""
11 container with most water
"""


class Solution(object):
	def get_most_water(self, height):
		if not height or len(height) < 2:
			return 0
		max_area = 0
		l, h = 0, len(height) - 1
		while l < h:
			max_area = max(max_area, (h - l) * min(height[l], height[h]))
			if height[l] < height[h]:  # while height[l]<=height[h] and l<h: l+=1
				l += 1
			else:  # while height[l]<=height[h] and l<h: h-=1
				h -= 1
		return max_area
