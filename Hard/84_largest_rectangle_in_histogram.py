"""
Largest rectangle in histogram
"""


def findLargestRectangle(heights):
	if not heights:
		return 0
	n = len(heights)
	higherFromLeft = [0] * n  # the first left element that is lower than i
	higherFromRight = [0] * n  # the first right element that is lower than i
	higherFromLeft[0] = -1
	higherFromRight[n - 1] = n

	for i in range(1, n):
		p = i - 1
		while p >= 0 and heights[p] >= heights[i]:
			p = higherFromLeft[p]
		higherFromLeft[i] = p

	for i in range(n - 2, -1, -1):
		p = i + 1
		while p < n and heights[p] >= heights[i]:
			p = higherFromRight[p]
		higherFromRight[i] = p

	res = 0
	for i in range(n):
		res = max(res, heights[i] * (higherFromRight[i] - higherFromLeft[i] - 1))
	return res


assert findLargestRectangle([1, 2, 3]) == 4
