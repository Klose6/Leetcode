"""
457 circular array loop
https://leetcode.com/problems/circular-array-loop/description/
https://leetcode.com/problems/circular-array-loop/discuss/94148
"""

class Solution(object):
  def circular_array_loop(self, nums):
     if not nums:
       return
     def move(pos):
       next = nums[pos] + pos
       if next < 0:
         next += len(nums)
       elif next >= len(nums):
         next %= len(nums)
       return next
     for i in range(len(nums)):
       if nums[i] == 0:
         continue
       slow, fast = i, i
       while nums[i]*nums[slow]>0 and nums[i]*nums[fast]>0:
         slow = move(slow)
         fast = move(move(fast))
         if slow == fast:
           if slow == move(slow): # one item loop
             break
           return True # find a loop
       # set all the elements along the path to 0
       slow = i
       sgn = nums[slow]
       while sgn * nums[slow] > 0:
         fast = move(slow)
         nums[slow] = 0
         slow = fast
     return False

print(Solution().circular_array_loop([2,-1,1,2,2])) # True
print(Solution().circular_array_loop([-1,2])) # False