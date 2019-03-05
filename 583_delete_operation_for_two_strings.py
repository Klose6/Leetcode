"""
583 delete operation fro two strings
"""


def minDistance(s1, s2):
  # find the longest common sub-sequence of them
  m, n = len(s1), len(s2)
  dp = [[0] * (n + 1) for _ in range(m + 1)]
  for i in range(m + 1):
    for j in range(n + 1):
      if i == 0 or j == 0:
        dp[i][j] = 0
      else:
        dp[i][j] = dp[i - 1][j - 1] + 1 if s1[i - 1] == s2[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
  return m + n - 2 * dp[i][j]


assert minDistance("tea", "eat") == 2
