"""
780 reaching points
"""

class Solution(object):
	def reaching_points(self, sx, sy, tx, ty):
		while tx>=sx and ty>=sy:
			if tx>=ty:
				if sy==ty:
					return (tx-sx)%ty==0
				tx%=ty
			else:
				if sx==tx:
					return (ty-sy)%sx==0
				ty%=tx
		return False
