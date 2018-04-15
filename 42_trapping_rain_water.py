"""
42 trapping rain water
"""
class Solution(object):
	def trapping_waters(self, nums):
		if not nums or len(nums)<=2:
			return
		n=len(nums)
		lmax, rmax= nums[0], nums[n-1]
		i, j = 0, n-1
		res = 0
		while i<=j:
			if nums[i] >= nums[j]:
				if rmax > nums[j]:
					res += rmax - nums[j]
				rmax=max(rmax, nums[j])
				j-=1
			else:
				if lmax > nums[i]:
					res += lmax - nums[i]
				lmax=max(lmax, nums[i])
				i+=1
		return res

s=Solution()
print s.trapping_waters([0,1,0,2,1,0,1,3,2,1,2,1]) #6