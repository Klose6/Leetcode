"""
560 subarray equals K
"""


def find_subarrays(nums, k):
  """
  compute all the prefix-sum and find the number of target sum = prefix_sum2 - prefix_sum1
  """
  res = pre_sum = 0
  dic = {0: 1}
  for i in nums:
    pre_sum += i
    res += dic.get(pre_sum - k, 0)
    dic[pre_sum] = dic.get(pre_sum, 0) + 1
  return res


print(find_subarrays([1, 1, 1], 2))  # 2
