"""
493 reverse pairs

https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22
"""

class Solution:

  def reversePairs(self, nums):
    if not nums or len(nums) < 2: return 0
    return self.merge_sort(nums, 0, len(nums)-1)

  def merge_sort(self, array, start, end):
    # print(f"{array}, {start}, {end}")
    if start >= end: return 0
    mid = (start + end) // 2
    count = self.merge_sort(array, start, mid) + self.merge_sort(array, mid+1, end)
    i, j, p, k = start, mid+1, mid+1, 0
    tmp = [0] * (end-start+1)
    while i <= mid:
      while j <= end and array[i] > 2*array[j]: # find all the number j that satisfy the condition for i
        j += 1
      count += j-(mid+1) # add the number of j
      while p <= end and array[i] > array[p]: # merge the two subarray, start from right side
        tmp[k] = array[p]
        k += 1
        p += 1
      tmp[k] = array[i] # add the i
      k += 1
      i += 1
    while p <= end: # add the left elements for the right side if any
      # print(f"p: {j}, k:{k}, tmp: {tmp}")
      tmp[k] = array[j]
      k += 1
      p += 1
    array[start: end+1] = tmp[:] # copy the merge result
    return count # return the count

print(Solution().reversePairs([1,3,2,3,1])) # 2