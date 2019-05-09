"""
480 sliding window median
https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
"""
from bisect import *

class Solution(object):
	def sliding_window_medians(self, nums, k):
		if not nums or len(nums) < k:
			return
		win, medians = nums[:k], []
		win.sort()
		odd = k%2
		for i, v in enumerate(nums[k:], k):
			medians.append((win[k//2]+win[k//2+1])/2.0 if not odd else win[k//2]/1.0)
			win.pop(bisect_left(win, nums[i-k]))
			insort(win, nums[i])
			# print i, v
		medians.append((win[k//2]+win[k//2+1])/2.0 if not odd else win[k//2]/1.0)
		return medians
	def sliding_window_medians2(self, nums, k):
		if not nums or len(nums)<k:
			return

s=Solution()
print(s.sliding_window_medians([1,3,-1,-3], 3)) #[1,-1]
