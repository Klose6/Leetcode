"""
Maximum intervals overlap
https://www.geeksforgeeks.org/find-the-point-where-maximum-intervals-overlap/

Consider a big party where a log register for guests entry and exit times is maintained.
Find the time at which there are maximum guests in the party. Note that entries in
register are not in any order.
"""

class Solution(object):
	def get_max_overlap(self, arrl, exit):
		if not arrl or not exit:
			return
		arrl = sorted(arrl)
		exit = sorted(exit)
		i, j = 1, 0
		n = len(arrl)
		guest_in = 1
		max_guest = 0
		while i<n and j < n:
			if arrl[i] <= exit[j]:
				guest_in += 1
				max_guest = max(guest_in, max_guest)
				# can also save the max overlap time
				i+=1
			else:
				guest_in -= 1
				j+=1
		return max_guest

s=Solution()
print s.get_max_overlap([1,2,10,5,5], [4,5,12,9,12]) #3