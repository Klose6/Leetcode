"""
Relative Ranks 506

"""


def relative_rank(nums):
  if not nums:
    return
  sorted_nums = sorted(nums)[::-1]
  ranks = ["Gold", "Silver", "Bronze"] + list(map(str, range(4, len(nums)+1)))
  return list(map(dict(zip(sorted_nums, ranks)).get, nums))

print(relative_rank([5,4,3,2,1]))