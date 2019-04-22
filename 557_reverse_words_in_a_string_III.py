"""
557 reverse words in a string III
"""

def reverse_words(s):
  # reverse the whole string list, then reverse the whole concatenated string
  if not s: return
  return " ".join(s.split()[::-1])[::-1]

# hello word!
# -> words! hello
# -> 0lleh !sdrow