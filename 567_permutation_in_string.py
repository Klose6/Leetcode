"""
567 permutation in string
"""


def containsPermutation(s1, s2):
  A = [ord(s) - ord('a') for s in s1]
  B = [ord(s) - ord('a') for s in s2]
  target = [0] * 26
  for x in A:
    target[x] += 1
  window = [0] * 26
  for i, x in enumerate(B):
    window[x] += 1
    if i >= len(A):
      window[B[i - len(A)]] -= 1
    if window == target:
      return True
  return False


print(containsPermutation("ab", "ebat"))
