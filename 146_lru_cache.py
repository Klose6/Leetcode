"""
146 LRU cache
"""
class Node(object):
	def __init__(self, key, val):
		self.key, self.val = key, val
		self.pre, self.next = None, None

class Solution(object):
	def __init__(self, capacity):
		self.capacity = capacity
		self.dic = dict()
		self.head = Node(0)
		self.tail = Node(0)
		self.head.next=self.tail
		self.tail.pre = self.head
	def get(self, key):
		if key in self.dic:
			n = self.dic.get(key)
			self._remove(n)
			self._add(n)
			return n.val
		return -1
	def set(self, key, val):
		if key in self.dic:
			self._remove(self.dic.get(key))
		n = Node(key, val)
		self._add(n)
		self.dic[key] = n
		if len(self.dic) > self.capacity:
			d = self.head.next
			self._remove(d)
			del self.dic[d.key]
	def _remove(self, node):
		node.pre.next = node.next
		node.next.pre = node.pre
	def _add(self, node):
		p = self.tail.pre
		p.next = node
		node.pre = p
		self.tail.pre = p
		node.next = self.tail
