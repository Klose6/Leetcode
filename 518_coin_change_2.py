"""
518 coin change 2
"""

def change(amount, coins):
  dp = [0] * (amount+1)
  dp[0] = 1 # initialize the array
  for c in coins:
    for i in range(1, amount+1):
      if i >= c: # for each single coin amount c, all the index divisible by c will be assigned 1
        dp[i] += dp[i-c]
  return dp[amount]

print(change(5, [1,2,5])) #4