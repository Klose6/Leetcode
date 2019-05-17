"""
472 concatenated words
"""

def findAllConcatenatedWords(words):
  if not words or len(words) < 3:
    return []
  words.sort(key=len) # sort the words by length
  preWords = set()
  res = []
  for w in words: # use all the shorter words as dict to check
    if canForm(w, preWords) == 1:
      res.append(w)
    preWords.add(w)
  return res

def canForm(w, preWords):
  print(f"{w}, {preWords}")
  if not preWords: return 0
  n = len(w)
  dp = [1] + [0]*n # dp[i]: whether the length i starts from 0 can be formed or not
  for i in range(1, n+1):
    for j in range(i)[::-1]:
      if w[j:i] in preWords and dp[j]:
        dp[i] = 1
        break
  return dp[n]

print(findAllConcatenatedWords(["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
# ['dogcatsdog', 'catsdogcats', 'ratcatdogcat']