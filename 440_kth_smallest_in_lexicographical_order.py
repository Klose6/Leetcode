"""
440 kth smallest in lexicographical order
https://leetcode.com/problems/k-th-smallest-in-lexicographical-order/discuss/92242/ConciseEasy-to-understand-Java-5ms-solution-with-Explaination
"""

def findKthNumber(n, k):
  res = 1
  k -= 1
  while  k>0:
    count = 0
    cur, next = res, res + 1
    while cur <= n: # find all the childeren nodes for cur, 1->10->100
      count += min(n+1, next) - cur
      cur *= 10
      next *= 10
    if count <=k:
      res += 1
      k-=count
    else:
      res*=10
      k-=1
  return res

print(findKthNumber(13, 2)) # 10
print(findKthNumber(10, 3)) # 2