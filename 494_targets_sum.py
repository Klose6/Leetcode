"""
494 target sum
"""
#https://leetcode.com/problems/target-sum/#/solutions
#https://discuss.leetcode.com/topic/76205/python-dp
"""
find a subset of the nums that need to be positive and the left to be negative so that the sum is the target
sum(P) - sum(N) = target
sum(P) - sum(N) + sum(P) + sum(N) = target + sum(P) + sum(N)
2 * sum(P) = target + sum(P) + sum(N)
"""

def findTargetSum(num, s):
  if not num:
    return -1
  sm = sum(num)
  if sm < s or (sm+s) % 2:
      return 0
  s += sm
  s = s // 2
  dp = [0] * (s+1)
  dp[0] = 1
  for i in num:
      for j in range(i, s+1)[::-1]:# we need the old states of i and i-1, so need to do it reversely
          dp[j] += dp[j-i]
      # print(f"dp: {dp}")
  return dp[s]

def findTargetSum2(nums, S): # relatively easier to understand
  count = {0: 1}
  for n in nums:
    count2 = {}
    for tmp in count: # find the frequency of all the sums when uses a new number
      count2[tmp + n] = count2.get(tmp + n, 0) + count[tmp]
      count2[tmp - n] = count2.get(tmp - n, 0) + count[tmp]
    count = count2
  print(f"count len: {count}")
  return count.get(S, 0)

# testing
print(findTargetSum([1,1,1,1,1], 3)) # 5
print(findTargetSum2([1,1,1,1,1], 3)) # 5