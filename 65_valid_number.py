"""
65 valid number
"""


def valid_number(s):
	s = s.strip()
	point = False
	e = False
	number = False
	number_after_e = True
	for i in range(len(s)):
		if s[i].isdigit():
			number = True
			number_after_e = True
		elif s[i] == ".":
			if e or point:
				return False
			point = True
		elif s[i] == "e":
			if e or not number:
				return False
			e = True
			number_after_e = False
		elif s[i] == "-" or s[i] == "+":
			if i != 0 or s[i - 1] != "e":
				return False
		else:
			return False
		return number and number_after_e
