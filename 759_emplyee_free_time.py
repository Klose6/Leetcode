"""
759 employee free time
"""

class Solution(object):
	def getfreetime(self, schedule):
		if not schedule:
			return
		intervals = []
		for s in schedule:
			intervals.extend(s)
		intervals = sorted(intervals, key=lambda x:x[0])
		# print intervals
		pre = [1, 1]
		res = []
		for inter in intervals:
			if inter[0] > pre[1]:
				res.append([pre[1], inter[0]])
				pre = inter
			else:
				pre = pre if pre[1] > inter[1] else inter
		return res
s=Solution()
print s.getfreetime([[[1,2], [5,6]], [[1,3]], [[4,10]]]) # [[3,4]]
print s.getfreetime([[[1,3], [6,7]], [[2,4]], [[2,5],[9,12]]]) #[[5,6],[7,9]]