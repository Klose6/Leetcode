"""
393 UTF-8 validation
"""

class Solution(object):
	def validate(self, data):
		if not data:
			return True
		count = 0
		for c in data:
			if count == 0:
				if c>>5 == int("110", 2):
					count = 1
				elif c>>4 == int("1110", 2):
					count =2
				elif c>>3==int("11110", 2):
					count =3
				elif c>>7:
					return False
			else:
				if c>>6 != int("10", 2):
					return False
				count-=1
		return count == 0

s=Solution()
print s.validate([197,130,1]) #True
print s.validate([235,140,4]) #False