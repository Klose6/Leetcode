"""
23 merge k sorted lists
"""
from Queue import PriorityQueue

class Node(object):
	def __init__(self, val):
		self.val = val
		self.next = None

class Solution(object):
	def merge_k_sorted_lists(self, lists):
		if not lists:
			return
		q = PriorityQueue()
		cur=dummy=Node(0)
		for head in lists:
				q.put((head.val, head))
		# res = []
		while q.qsize() > 0:
			cur.next = q.get()[1]
			cur=cur.next
			# res.append(cur.val)
			if cur.next:
				q.put((cur.next.val, cur.next))
		# print res
		return dummy.next

s=Solution()
n1 = Node(1)
n2=Node(3)
n3=Node(2)
n1.next=n2
s.merge_k_sorted_lists([n1, n3])