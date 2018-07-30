"""
84 largest rectangle in histogram

The stack maintain the indexes of buildings with ascending height.
Before adding a new building pop the building who is taller than
the new one. The building popped out represent the height of a
rectangle with the new building as the right boundary and the
current stack top as the left boundary. Calculate its area and
update ans of maximum area. Boundary is handled using dummy
buildings
"""


def largest_rectangle(heights):
	res = 0
	stack = [-1]  # in case when the len(stack) == 1 for line 21
	heights.append(0)  # add one more element for final check
	for i in range(len(heights)):
		while heights[i] < heights[stack[-1]]:
			h = heights[stack.pop()]
			w = i - stack[-1] - 1
			res = max(res, h * w)
		stack.append(i)
	heights.pop()
	return res


print largest_rectangle([2, 1, 5, 6, 2, 3])  # 10
