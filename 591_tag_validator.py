"""
591 tag validator
"""


class Solution(object):
	def tag_validator(self, code):
		stack = []
		i, n = 0, len(code)
		while i < n:
			if not stack and i > 0: return False
			if code.startswith("<![CDATA[", i):
				j = i + 9
				i = code.index("]]>", j)
				if i < 0: return False
				i += 3
			elif code.startswith("</", i):
				j = i + 2
				i = code.index(">", j)
				if i < 0 or i == j or i - j > 9: return False
				for k in range(j, i):
					if code[k].islower(): return False
				if not stack or stack.pop() != code[j:i]:
					return False
				i += 1
			elif code.startswith("<", i):
				j = i + 1
				i = code.index(">", j)
				if i < 0 or i == j or i - j > 9: return False
				for k in range(j, i):
					if code[k].islower(): return False
				stack.append(code[j:i])
				i += 1
			else:
				i += 1
		return len(stack) == 0


print Solution().tag_validator("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
