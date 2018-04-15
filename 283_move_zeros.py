"""
https://discuss.leetcode.com/topic/24716/simple-o-n-java-solution-using-insert-index
"""
def move_zeros(nums):
  if not nums:
    return
  cur = 0
  for i in range(len(nums)):
    if nums[i] == 0:
      nums[cur], nums[i] = nums[i], nums[cur]
      cur += 1


nums = [0,1,0,3,12]
nums = [0,0]
move_zeros(nums)
print(nums)
