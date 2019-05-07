"""
486 predict the winner
"""

def predictWinner(nums):
  """ recursive"""
  if not nums: raise ValueError("Wrong input")
  def helper(array, s, e):
    return array[s] if s == e else max(array[e] - helper(array, s, e-1), array[s] - helper(array, s+1, e))
  return helper(nums, 0, len(nums)-1) >= 0


def predictWinner2(nums):
  n = len(nums)
  if n % 2 == 0: return True
  # dp[i][j]: how much more scores the first player can get than the second player
  dp = [[0] * n for _ in range(n)]
  for i in range(n):
    dp[i][i] = nums[i]
    for j in range(i-1, -1, -1):
        dp[j][i] = max(nums[j] - dp[j+1][i], nums[i] - dp[j][i-1])
  return dp[0][n-1] >= 0

print(predictWinner2([1, 7, 5])) # False
print(predictWinner2([1, 5, 7])) # True