"""
480 sliding window median
https://leetcode.com/problems/sliding-window-median/discuss/96337/Python-SortedArray-(beats-100)-and-2-Heap(beats-90)-solution
"""
from bisect import *
from heapq import heappush, heappop

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
		if not nums or len(nums) < k:
			return
		lh, rh = [], []
		res = []
		for i, v in enumerate(nums[:k]):
			heappush(lh, (-v, i))
		for i in range(k - k//2):
			val, idx = heappop(lh)
			heappush(rh, (-val, idx))
		for i, v in enumerate(nums[k:], k):
			print(f"lh: {lh}, rh: {rh}")
			res.append(rh[0][0]/1.0 if k%2 else (rh[0][0]-lh[0][0])/2.0)
			# remove the (i-k) element
			if v >= rh[0][0]:
				heappush(rh, (v, i))
				if nums[i-k] <= rh[0][0]:
					val, idx = heappop(rh)
					heappush(lh, (-val, idx))
			else:
				heappush(lh, (-v, i))
				if nums[i-k] >= rh[0][0]:
					val, idx = heappop(lh)
					heappush(rh, (-val, idx))
			# adjust the heap
			print(f"before adjust: {lh}, {rh}")
			# no need to delete the i-k element immediately for each iteration except it's on the top of the heaps
			while lh and lh[0][1] <= i-k: heappop(lh)
			while rh and rh[0][1] <= i-k: heappop(rh)
		res.append(rh[0][0] / 1.0 if k % 2 else (rh[0][0] - lh[0][0]) / 2.0)
		return res


s=Solution()
# print(s.sliding_window_medians([1,3,-1,-3], 3)) #[1,-1]
# print(s.sliding_window_medians2([1,3,-1,-3], 3)) #[1, -1]

# print(s.sliding_window_medians2([10,2], 1)) # [1,2]
print(s.sliding_window_medians2([9,7,0,3,9,8,6,5,7,6], 2))

# print(s.sliding_window_medians2([1,3,-1,-3,5,3,6,7], 3)) # [1.0,-1.0,-1.0,3.0,5.0,6.0]
