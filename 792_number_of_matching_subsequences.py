import collections


def numMatchingSubseq(S, words):
  waiting = collections.defaultdict(list)
  for w in words:
    waiting[w[0]].append(iter(w[1:]))
  for s in S:
    for c in waiting.pop(s, ()):
      waiting[next(c, None)].append(c)
  return len(waiting[None])


print(numMatchingSubseq("abcde", ["a", "bb", "acd", "ace"]))  # 3
