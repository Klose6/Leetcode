"""
Next greater elements II 503
https://leetcode.com/problems/next-greater-element-ii/#/discuss
"""

def nextGreaterElements(nums):
  stack, res = [], [-1] * len(nums)
  for i in list(range(len(nums)))*2:
    while stack and nums[stack[-1]] < nums[i]: # find all the bigger number for all the elements
      res[stack.pop()] = i # may update the same item in res twice, but that is fine
    stack.append(i)
  return res

print(nextGreaterElements([1,2,1]))
# print(list(range(2)))
