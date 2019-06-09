"""
448 find all number disappeared in an array
"""

def find_all_disappaared_numbers(nums):
  if not nums: return []
  # mark all the elements that we have seen as negative
  for i, v in enumerate(nums):
    if nums[abs(v)-1] > 0:
      nums[abs(v)-1] = -nums[abs(v)-1]
  # find all the not seen elements
  return [ i+1 for i, v in enumerate(nums) if v > 0]


print(find_all_disappaared_numbers([4,3,2,7,8,2,3,1])) # [5,6]