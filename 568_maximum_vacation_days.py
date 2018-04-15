"""
568 maximum vacation days
"""
class Solution(object):
	def maxvacationdays(self, flights, days):
		"""
		dp[i][j] stands for the max vacation days we can get in week i
		staying in city j. Itis obvious that
		 dp[i][j] = max(dp[i - 1][k] + days[j][i])
		 (k = 0...N - 1, if we can go from city k to city j)
		"""
		if not flights or not days:
			return 0
		ninf = float("-inf")
		m, n=len(days), len(days[0])
		dp = [ninf]*n
		dp[0]=0
		for k in range(n):
			cur = [ninf]*n
			for i in range(m): # for every i->j
				for j in range(m):
					if i==j or flights[j][i]:
						cur[i] = max(cur[i], days[j][k]+dp[i])
			dp = cur
		return max(dp)
s= Solution()
flights = [[int(i) for i in j] for j in "011\n101\n110".splitlines()]
days = [[int(i) for i in j] for j in "131\n603\n333".splitlines()]
print s.maxvacationdays(flights, days) #12