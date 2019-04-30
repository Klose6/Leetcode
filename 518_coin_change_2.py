"""
518 coin change 2
"""

def change(amount, coins):
  dp = [0] * (amount+1)
  dp[0] = 1 # initialize the array
  for c in coins:
    for i in range(c, amount+1):
      # for each single coin amount c, all the index divisible by c will be assigned 1
      # the number of combinations of amount i equals the sum of all the less amount
      dp[i] += dp[i-c]
  return dp[amount]

print(change(5, [1,2,5])) #4