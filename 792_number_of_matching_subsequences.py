import collections


def numMatchingSubseq(S, words):
  # Time complexity: O(S + #words)
  # Space complexity: O(#words)
  waiting = collections.defaultdict(list)
  for w in words:  # O(#words)
    waiting[w[0]].append(iter(w[1:]))
  for s in S:  # O(S)
    for c in waiting.pop(s, ()):  # each word will only be popped and added to the dict once for each loop
      waiting[next(c, None)].append(c)
  return len(waiting[None])


print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # 3
