"""
853 car fleet

Calculate time needed to arrive the target, sort by the start position.
Loop on each car from the end to the beginning. cur record the current biggest time (the slowest).
If another car needs less or equal time than cur, it can catch up this car.
Otherwise it will become the new slowest car, that is new lead of a car fleet.
"""


class Solution(object):
	def car_fleet(self, speeds, positions, target):
		times = [float(target - p) / s for p, s in sorted(zip(positions, speeds))]
		res = cur = 0
		for time in times[::-1]:
			if cur < time:
				res += 1
				cur = time
		return res
