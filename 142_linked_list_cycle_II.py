"""
142 linked list cycle II
"""


def detect_cycle(head):
	if not head or not head.next: return None
	slow, fast = head, head
	is_cycle = False
	while slow and fast:
		slow = slow.next
		if not fast.next: return None
		fast = fast.next.next
		if slow == fast:
			is_cycle = True
			break
	if not is_cycle: return None
	slow = head
	while slow != fast:
		slow = slow.next
		fast = fast.next
	return slow
