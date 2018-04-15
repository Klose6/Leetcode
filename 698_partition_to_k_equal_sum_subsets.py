"""
698 partition to k equal sum subsets
https://discuss.leetcode.com/topic/107600/clean-python-dfs-beats-90
https://discuss.leetcode.com/topic/107185/java-c-straightforward-dfs-solution
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/solution/
"""

def partition_k(nums, k):
  if k == 1:
    return True
  if sum(nums) % k != 0:
    return False
