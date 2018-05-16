"""
91 decode ways
"""


def num_decoding(s):
	if not s or s[0] == '0':
		return 0
	# decode ways of s[i-2] and s[i-1]
	pre2, pre1 = 1, 1
	for i in range(1, len(s)):
		# 0 valid ways of the last since 0 cannot be used separately
		if s[i] == '0':
			pre1 = 0
		# possible two digits letters, so pre1 will be the sum and pre2 will the old pre1
		if s[i - 1] == '1' or s[i - 1] == '2' and s[i] <= '6':
			pre1 = pre1 + pre2
			pre2 = pre1 - pre2
		else:
			# only one way to decode
			pre2 = pre1
	return pre1


print num_decoding("12")  # 2
print num_decoding("226")  # 2
