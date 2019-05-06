"""
488 zuma game
https://leetcode.com/problems/zuma-game/discuss/97010/%22short%22-java-solution-beats-98
"""
from collections import Counter
from sys import maxsize

res = maxsize

def findMinStep(board, hand):
  counter = Counter(hand)
  global res
  res = dfs(board + "#", counter) # addd "#" to the end for the corner case
  return res if res != maxsize else -1

def dfs(s, counter):
  s = removeConsecutive(s)
  if s == "#": return 0
  j = 0
  for i in range(len(s)):
    if s[i] == s[j]: continue
    need = 3 - (i - j) # get the number of chars needs to add
    if s[j] in counter and need <= counter[s[j]]:
      counter[s[j]] = counter[s[j]] - need # remove the number of chars for the map
      # print(f"next: {s[:j] + s[i:]}, counter: {counter}")
      global res
      res = min(res, need + dfs(s[:j] + s[i:], counter)) # dfs to the next iteration
      # print(f"res: {res}")
      counter[s[j]] = counter[s[j]] + need # add the number back for the number iteration
    j = i # try to find the next elements to remove
  return res

def removeConsecutive(board):
  # remove the >=3 consecutive elements in the board
  j = 0
  for i in range(len(board)):
    if board[i] == board[j]: continue
    elif i - j >= 3:
      return removeConsecutive(board[:j] + board[i:])
    else:
      j = i
  return board

# testing
print(findMinStep("WRRBBW", "RB")) # -1
print(findMinStep("WWRRBBWW", "WRBRW")) # 2