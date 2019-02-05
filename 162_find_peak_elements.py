"""
162 find peak elements
"""

class Solution(object):
	def find_peak_elements(self, nums):
		if not nums:
			return
		lo, hi = 0, len(nums)-1
		while lo < hi:
			mid = lo+(hi-lo)/2
			mid2 = mid+1
			if nums[mid] < nums[mid2]:
        lo = mid2
			else:
        hi = mid
		return nums[lo]

  def find_peak_elements1(self, nums):
    if not nums:
      return
    n = len(nums)
    for i in range(1, n):
      if nums[i] < nums[i - 1]:
        return nums[i - 1]
    return nums[n - 1]

s=Solution()
assert s.find_peak_elements([1]) == 1
assert s.find_peak_elements([1, 2]) == 2
assert s.find_peak_elements([2, 1]) == 2
assert s.find_peak_elements([1, 3, 2]) == 3

assert s.find_peak_elements1([1]) == 1
assert s.find_peak_elements1([1, 2]) == 2
assert s.find_peak_elements1([2, 1]) == 2
assert s.find_peak_elements1([1, 3, 2]) == 3
