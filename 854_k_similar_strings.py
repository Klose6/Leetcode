"""
854 K similar strings
"""
import collections


class Solution(object):
	def num_swaps(self, A, B):
		if A == B:
			return 0

		def neighbors(S):
			for i, c in enumerate(S):
				if B[i] != c:
					break
			T = list(S)
			for j in range(i + 1, len(S)):
				if S[j] == B[i]:
					T[i], T[j] = T[j], T[i]
					yield "".join(T)
					T[j], T[i] = T[i], T[j]

		q = collections.deque([A])
		seen = {A: 0}
		while q:
			cur = q.popleft()
			if cur == B:
				return seen[B]
			for nei in neighbors(cur):
				if nei not in seen:
					q.append(nei)
					seen[nei] = seen[cur] + 1


print Solution().num_swaps("aabc", "abca")  # 2
