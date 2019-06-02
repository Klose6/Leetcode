"""
460 LFU cache
https://leetcode.com/problems/lfu-cache/description/
http://www.cnblogs.com/grandyang/p/6258459.html
https://leetcode.com/problems/lfu-cache/discuss/207673/Python-concise-solution-**detailed**-explanation%3A-Two-dict-%2B-Doubly-linked-list
"""

from collections import defaultdict

class Node(object):
	def __init__(self, key, val):
		self.key = key
		self.val = val
		self.fred = 1
		self.pre = self.next = None

class DoubleLinkedList:
	def __init__(self):
		self.dummy = Node(None, None)
		self.dummy.pre = self.dummy.next = self.dummy
		self.size = 0

	def append(self, node):
		node.next = self.dummy.next
		node.next.pre = node
		self.dummy.next = node
		node.prev = self.dummy
		self.size += 1

	def pop(self, node=None):
		if self.size == 0:
			return
		if not node:
			node = self.dummy.pre
		node.pre.next = node.next
		node.next.pre = node.pre
		self.size -= 1
		return node

class LFUCache:
	def __init__(self, capacity):
		self.size = 0
		self.capacity = capacity
		self.node = dict() # key: node
		self.freq = defaultdict(DoubleLinkedList)
		self.min_freq = 0

	def _update(self, node):
		# helper function ro remove the old node and add it to the new freq list
		freq = node.freq
		self.freq[freq].pop(node)
		if self.min_freq == freq and not self.freq:
			# if the removed node is the only node in the freq list, need to update the min_freq
			self.min_freq += 1
		node.freq += 1
		freq = node.freq
		self.freq[freq].append(node)

	def get(self, key):
		if key not in self.node:
			return -1
		node = self.node[key]
		self._update(node)
		return node.val

	def put(self, key, value):
		if self.capacity == 0:
			return
		if key in self.node:
			node = self.node[key]
			self._update(node)
			node.val = value
		else:
			if self.size == self.capacity:
				node = self.freq[self.min_freq].pop()
				del self.node[node.key]
				self.size -= 1
			node = Node(key, value)
			self.node[key] = node
			self.freq[1].append(node)
			self.min_freq = 1
			self.size += 1