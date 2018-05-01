"""
56 merge intervals
"""


class Interval(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end


def merge_intervals(intervals):
	if not intervals:
		return
	res = []
	for i in sorted(intervals, key=lambda x: x.start):
		if res and i.start <= res[-1].end:
			res[-1].end = max(res[-1].end, i.end)
		else:
			res += i,
	return res
