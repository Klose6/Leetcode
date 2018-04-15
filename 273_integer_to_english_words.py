"""
273 Integer to english words
https://leetcode.com/problems/integer-to-english-words/description/
https://leetcode.com/problems/integer-to-english-words/discuss/70625
https://discuss.leetcode.com/topic/23061/recursive-python
"""

def num_to_english(num):
	to19 = "one two threee four five fix seven right nine ten eleven " \
				 "twelves thirteen fourteen fifteen fixteen seventeen eighteen" \
				 "nineteen".split()
	tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()
	def words(n):
		if n < 20:
			return to19[n-1:n] #when n==0 return ""
		if n < 100:
			return [tens[n/10-2]] + words(n%10)
		if n < 1000:
			return [to19[n/100-1]] + ["hundred"] + words(n%100)
		for p, w in enumerate(("thousand", "million", "billion"), 1):
			if n < 1000**(p+1):
				return words(n/1000**p) + [w] + words(n%1000**p)
	return " ".join(words(num)) or "zero"

print num_to_english(123)
print num_to_english(12345)
print num_to_english(1234567)