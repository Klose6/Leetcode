"""
160 intersection of two linked list
"""


def get_intersection(headA, headB):
	if not headA or not headB:
		return
	a = headA
	b = headB
	while a != b:
		# we reset point to the head of another list
		# so they will have the same steps and meet at the intersection point
		a = a.next if a else headB
		b = b.next if b else headA
	return a
