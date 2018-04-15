import re
"""
https://discuss.leetcode.com/topic/77793/one-liner-ruby-python
https://discuss.leetcode.com/topic/78213/solution-in-python-using-set
"""

def find_words(words):
  return filter(re.compile('(?i)([qwertyuiop]*|[asdfghjkl]*|[zxcvbnm]*)$').match, words)

def find_words(words):
  res = []
  first = set("qwertyuiop")
  second = set("asdfghjkl")
  third = set("zxcvbnm")
  for word in words:
    word_low = set(word.lower())
    # if word_low.issubset(first) or word_low.issubset(second) or word_low.issubset(third):
    if word_low <= first or word_low <= second or word_low <= third:
      res.append(word)
  return res

words = ['abc', 'alaska']
print(find_words(words))
