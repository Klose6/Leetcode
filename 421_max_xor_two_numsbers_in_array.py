"""
421 Maximum XO or two numbers in a array
http://www.cnblogs.com/grandyang/p/5991530.html
"""

class Solution(object):
	def max_xor_two(self, nums):
		if not nums or len(nums) < 2:
			return
		res=0
		for i in range(32)[::-1]:
			prefix = {n>>i for n in nums}
			res <<= 1
			# a^b=c -> a=b^c
			res += any(res^1^p in prefix for p in prefix)
		return res
	def max_xor_two2(self, nums):
		"""
		build a trie to store all the 32 bit of all the nums, then
		for each num, search the trie to get the largest xor
		"""
		if not nums or len(nums)<2:
			return 0
		root = [None, None]
		for num in nums:
			cur = root
			for i in range(31,-1,-1):
				idx=int(num>>i&1)
				if not cur[idx]:
					cur[idx] = [None, None]
				cur=cur[idx]
		maxxor=0
		for num in nums:
			cur=root
			curxor=0
			for i in range(31,-1,-1):
				idx=int(num>>i&1)
				if cur[1^idx]:
					curxor|=1<<i
					cur=cur[1^idx]
				else:
					cur=cur[idx]
			maxxor=max(maxxor, curxor)
		return maxxor


s=Solution()
print s.max_xor_two([3,10,5,25,2,8]) #28
print s.max_xor_two2([3,10,5,25,2,8]) #28