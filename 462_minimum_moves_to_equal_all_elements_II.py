"""
462 minimum moves to equal array
"""
"""
find the median
"""
def minMoves(nums):
  if not nums or len(nums) < 2: return 0
  nums.sort()
  res = 0
  i, j = 0, len(nums)-1
  while i<j:
    res += nums[j] - nums[i]
    i += 1
    j -= 1
  return res


def minMoves2(nums):
  median = sorted(nums)[len(nums)//2]
  return sum(abs(num-median) for num in nums)

def minMoves3(nums):
  nums.sort() # ~ is the negative index for the index i
  return sum(nums[~i] - nums[i] for i in range(len(nums)//2))

print(minMoves([1,2,3])) # 2
print(minMoves2([1,2,3])) # 2
print(minMoves3([1,2,3])) #2