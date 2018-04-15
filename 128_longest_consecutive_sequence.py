"""
128 longest consecutive sequence
"""

class Solution(object):
	def get_longest_consecutive_seq(self, nums):
		if not nums:
			return
		s = set(nums)
		res = 0
		for n in nums:
			pre, next=n-1, n+1
			while pre in s:
				s.remove(pre)
				pre-=1
			while next in s:
				s.remove(next)
				next+=1
			s.add(n)
			res = max(res, next-pre-1)
		return res
	def get_longest_consecutive_seq2(self, nums):
		if not nums:
			return
		s=set(nums)
		res =0
		for n in s:
			if n-1 not in s:
				y=n+1
				while y in s:
					y+=1
				res=max(res, y-n)
		return res

s=Solution()
print s.get_longest_consecutive_seq([1,2,5,4,6])
print s.get_longest_consecutive_seq2([1,2,5,4,6])