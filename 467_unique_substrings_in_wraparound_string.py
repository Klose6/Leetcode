"""
467 unique substring in wraparound string
"""

def findSubstring(p):
  if not p: return 0
  dp = [0] * 26 # dp[i] is the maximum unique substring ends with ('a'+i)
  # the substring of consecutive chars "abc" ends with "c" is "abc", "bc", "c"
  maxLen = 0
  for i, v in enumerate(p):
    if i > 0 and (ord(p[i]) - ord(p[i-1]) == 1 or ord(p[i-1]) - ord(p[i]) == 25):
      maxLen += 1
    else:
      maxLen = 1
    idx = ord(v) - ord("a")
    dp[idx] = max(dp[idx], maxLen)
  return sum(dp)

print(findSubstring("a")) # 1
print(findSubstring("zab")) # 6