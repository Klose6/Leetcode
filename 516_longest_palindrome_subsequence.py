"""
516 longest palindrome subsequence
"""

def findLongestPalindrome(s):
  if not s: return 0
  n = len(s)
  # dp[i][j]: the longest palindrome from i to j
  dp = [[0]*n for _ in range(n)]
  for i in range(n)[::-1]:
    dp[i][i] = 1
    for j in range(i+1, n):
      if s[i] == s[j]:
        dp[i][j] = dp[i+1][j-1] + 2
      else:
        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
  return dp[0][n-1]

print(findLongestPalindrome("bbbab")) # 4
print(findLongestPalindrome("cbbd")) # 2