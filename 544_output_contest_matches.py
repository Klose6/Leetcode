"""
544 output contest matches
"""
import math

def contestMatches(n):
  if n < 2: return ""
  matches = [i for i in range(1, n+1)]
  # print(f"{matches}")
  # find the total number of iterations which is log2(n)
  for _ in range(int(math.log(n, 2))): # for each iteration, start from the left most and right most pairs until the middle
    matches = [f"({matches[i]}, {matches[len(matches)-i-1]})" for i in range(0, len(matches) // 2)]
    # print(f"matches: {matches}")
  return matches

print(contestMatches(8))
print(contestMatches(4))