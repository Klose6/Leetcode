"""
514 freedom trail
"""
import collections


class Solution(object):
	def freedom_trail(self, ring, key):
		m, n = len(ring), len(key)
		# the distance between two points in the ring
		def dist(a, b):
			return min(abs(a - b), m - abs(a - b))
		# build the position for each char in the ring
		pos = collections.defaultdict(list)
		for i, c in enumerate(ring):
			pos[c].append(i)
		# the current possible state to its cost, initially at the first char of the ring
		state = {0: 0}
		for k in key:
			next_state = {}
			# every possible target position
			for n in pos[k]:
				next_state[n] = float("inf")
				for j in state:  # every possible start position
					next_state[n] = min(next_state[n], dist(n, j) + state[j])
			state = next_state
		return min(state.values()) + len(key)

print Solution().freedom_trail("godding", "gd") == 4
