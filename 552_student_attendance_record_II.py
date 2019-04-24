"""
552 student attendance record II
"""


class Solution(object):
	def checkRecord(self, n):
		res = [""]
		for i in range(n):
			cur = []
			for r in res:
				if "A" not in r:
					cur.append(r + "A")
				if not (len(r) >= 2 and r[-1] == "L"):
					cur.append(r + "L")
				cur.append(r + "P")
			res = cur
		return res

	def checkRecord1(self, n):
		if n == 1: return 3
		m = 10 ** 9 + 7
		# P(n) is the total number of all possible attendance records ended with 'P' with length n.
		# L(n) is the total number of all possible attendance records ended with 'L' with length n.
		# A(n) is the total number of all possible attendance records ended with 'A' with length n.
		A, P, L = [0] * n, [0] * n, [0] * n
		P[0] = 1 # P[0] is actually n = 1
		L[0], L[1] = 1, 3
		A[0], A[1] = 1, 2,
		if n > 2:
			A[2] = 4
		for i in range(1, n):
			A[i - 1] %= m
			P[i - 1] %= m
			L[i - 1] %= m
			P[i] = ((A[i - 1] + P[i - 1]) % m + L[i - 1]) % m
			if i > 1: # if the (n-2)th char is A, can add LL; if the (n-2)th char is P can add LL; if the (n-2)th char is L, can't add LL
				L[i] = ((A[i - 1] + P[i - 1]) % m + (A[i - 2] + P[i - 2]) % m) % m
			if i > 2:
				# A(n) = noAP(n-1) + noAL(n-1); noAP(n) = noAP(n-1) + noAL(n-1); noAL(n)=noAP(n-1) + noAP(n-2)
				# => A(n) = A(n-1) + A(n-2) + A(n-3) since A(n) == noAP(n)
				A[i] = ((A[i - 1] + A[i - 2]) % m + A[i - 3]) % m
		return ((A[n - 1] % m + P[n - 1] % m) % m + L[n - 1] % m) % m


print(Solution().checkRecord(2))
print(Solution().checkRecord1(2))
