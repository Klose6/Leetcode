"""
460 LFU cache
https://leetcode.com/problems/lfu-cache/description/
http://www.cnblogs.com/grandyang/p/6258459.html
"""

class Node(object):
	val, count, next_node = 0, 0, None



class Solution(object):
	key_to_val = {}
	key_to_node = {}
	double_list = None
	def get_val(self, key):
		if key in self.key_to_val:
			return self.key_to_val[key]