#https://leetcode.com/problems/target-sum/#/solutions
#https://discuss.leetcode.com/topic/76205/python-dp
def findTargetSumWays(num, s):
  if not num:
    return -1
  sm = sum(num)
  if sm < s or (sm+s) % 2:
      return 0
  s += sm
  s = (int)(s/2)
  dp = [0]*(s+1)
  dp[0] = 1
  for i in num:
      for j in range(i, s+1)[::-1]:
          dp[j] += dp[j-i]
  return dp[s]

print(findTargetSumWays([1,1,1,1,1], 3))