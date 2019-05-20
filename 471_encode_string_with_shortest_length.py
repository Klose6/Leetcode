"""
471 encode string with shortest length

https://www.cnblogs.com/grandyang/p/6194403.html
"""


def encode(s):
  """
  dp[j][i]: the shortest encode string for s[j:i]
  """
  if not s: return ""
  n = len(s)
  dp = [[""]*n for _ in range(n)]
  for i in range(n):
    for j in range(i, -1, -1):
      t = s[j: i+1]
      dp[j][i] = t
      idx = (t+t).index(t, 1)
      if idx < len(t): # find a repeat pattern in t, then check whether it is the shortest encode
        p = f"{len(t) // idx}[{t[:idx]}]"
        dp[j][i] = p if len(p) < i-j+1 else t
        continue
      for k in range(j, i): # if there is not repeat pattern, then find the min encode by trying k for[j:k] and [k+1][i]
        if len(dp[j][k]) + len(dp[k+1][i]) < len(dp[j][i]):
          dp[j][i] = dp[j][k] + dp[k+1][i]
  return dp[0][n-1]

print(encode("aaa"))
print(encode("aaaaa"))
print(encode("aabcaabcd"))