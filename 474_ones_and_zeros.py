"""
474 ones and zeros
"""

def maxNumbers(strs, m, n):
  # dp[i][j]: the max number of string we can get by using i 1s and j 0s
  dp = [[0] * (m+1) for _ in range(n+1)]
  for s in strs:
    ones, zeros = 0, 0
    for i in s:
      if i == "1": ones += 1
      if i == "0": zeros += 1
    # reverse traversal to use the dp data from the last iteration
    for i in range(n, ones-1, -1):
      for j in range(m, zeros-1, -1):
        dp[i][j] = max(dp[i][j], dp[i-ones][j-zeros]+1)
  return dp[n][m]

print(maxNumbers(["10","1","0"], 1, 1)) # 2