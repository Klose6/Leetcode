"""
446 arithmetic slices II
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/92822/Detailed-explanation-for-Java-O(n2)-solution
https://leetcode.com/problems/arithmetic-slices-ii-subsequence/discuss/92852/11-line-Python-O(n2)-solution
"""
from collections import defaultdict

def numberOfArithmeticSlices(A):
  if not A or len(A) < 3: return 0
  res = 0
  dp = [defaultdict(int) for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(i):
      dp[i][A[i]-A[j]] += 1
      if A[i]-A[j] in dp[j]: # find a length 3 arithmetic slice
        dp[i][A[i]-A[j]] += dp[j][A[i]-A[j]]
        res += dp[j][A[i]-A[j]]
  return res

print(numberOfArithmeticSlices([2,4,6,8,10])) # 7