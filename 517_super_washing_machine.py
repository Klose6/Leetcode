"""
517 super washing machine
"""


class Solution(object):
	def super_washing_machine(self, machines):
		n = len(machines)
		if sum(machines) % n != 0: return -1
		count, res = 0, 0
		avg = sum(machines) / n
		for load in machines:
			count += load - avg
			res = max(res, max(load - avg, abs(count)))
		return res


print Solution().super_washing_machine([1, 0, 5]) == 3
print Solution().super_washing_machine([0, 3, 0]) == 2
