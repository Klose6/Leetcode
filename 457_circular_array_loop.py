"""
457 circular array loop
https://leetcode.com/problems/circular-array-loop/description/
https://leetcode.com/problems/circular-array-loop/discuss/94148
"""

class Solution(object):
  def circular_array_loop(self, nums):
     if not nums or len(nums) < 2: return False
     def move(nums, i):
       # print(f"idx: {i}")
       n = len(nums)
       return (nums[i]+i)%n
     for i in range(len(nums)):
       if nums[i] == 0:
         continue
       slow, fast = i, i
       while nums[i]*nums[slow]>0 and nums[i]*nums[fast]>0:
         slow = move(nums, slow)
         fast = move(nums, fast)
         if nums[i] * nums[fast] <= 0: break # check the middle step direction
         fast = move(nums, fast)
         # print(f"slow, fast: ({slow}, {fast})")
         if slow == fast:
           if slow == move(nums, slow): # one item loop
             break
           return True # find a loop
       # set all the elements along the path to 0 if loop not found
       slow = i
       sgn = nums[slow]
       while sgn*nums[slow] > 0:
         fast = move(nums, slow)
         nums[slow] = 0
         slow = fast
     return False

print(Solution().circular_array_loop([2,-1,1,2,2])) # True
print(Solution().circular_array_loop([-1,2])) # False
print(Solution().circular_array_loop([1,1,1,1,1,1,1,1,1,-5])) # False