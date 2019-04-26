"""
540 single element in a sorted array
"""

def singleElement(nums):
  if not nums: raise ValueError("Input error")
  l, r = 0, len(nums)-1
  # because the single element, then start from the single element, then even ith element != (i+1)th elemen
  while l < r:
    mid = l + (r - l) // 2
    if mid % 2 == 1: # always start the even index
      mid -= 1
    if nums[mid] != nums[mid+1]: # we din't find a pair, then the target must on the left side
      r = mid
    else: # then the target must on the right side - mid + 2
      l = mid + 2
  return nums[l]

print(singleElement([1,1,2,3,3,4,4,8,8])) # 2
print(singleElement([3,3,7,7,10,11,11])) # 10
