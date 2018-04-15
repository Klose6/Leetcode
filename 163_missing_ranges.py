"""
163 missing ranges
"""

class Solution(object):
	def get_missing_ranges(self, nums, lower, upper):
		if not nums or lower > upper:
			return
		pre=lower-1
		res= []
		nums.append(upper+1)
		for i in nums:
			if i==pre+2:
				res.append(str(pre+1))
			elif i>pre+2:
				res.append(str(pre+1)+"->"+str(i-1))
			pre=i
		return res
s=Solution()
print s.get_missing_ranges([0,1,3,50,75], 0,99)