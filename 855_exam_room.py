"""
855 exam room
"""
import bisect

class ExamRoom(object):
	def __init__(self, N):
		# L to record the seats that people sit
		self.N, self.L = N, []

	def seat(self):
		N, L = self.N, self.L
		if not L:
			return 0
		else:
			d, res = L[0], 0
			for a, b in zip(L, L[1:]):
				if (b - a) / 2 > d:
					d, res = (b - a) / 2, (b + a) / 2
			if N - 1 - L[-1] > d:
				res = N - 1
		bisect.insort(L, res)
		return res

	def leave(self, p):
		self.L.remove(p)
