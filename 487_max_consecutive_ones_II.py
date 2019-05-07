"""
487 max consectuive ones II

https://www.cnblogs.com/grandyang/p/6376115.html
"""

def maxConsectiveOnes(nums):
  if not nums: return 0
  res = 0
  count, cur = 0, 0 # need to store the 1's count for two sections separated by one 0
  for i in nums:
    count += 1
    if i == 0:
      cur = count
      count = 0
    res = max(res, cur + count)
  return res


from queue import Queue

def maxConsecutiveOnesK(nums, k):
  # what if we can turn maximum k 0s
  if not nums: return 0
  q = Queue()
  res, left = 0, 0
  for i in nums:
    if i == 0:
      q.put(i)
    if q.qsize() > k:
      left = q.get() + 1
    res= max(res, i - left +1)
  return res

print(maxConsectiveOnes([1,0,1,1,0])) # 4