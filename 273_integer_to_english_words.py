"""
273 Integer to english words
https://leetcode.com/problems/integer-to-english-words/description/
https://leetcode.com/problems/integer-to-english-words/discuss/70625
https://discuss.leetcode.com/topic/23061/recursive-python
"""

def num_to_english(num):
	to19 = "one two three four five fix seven right nine ten eleven " \
				 "twelves thirteen fourteen fifteen sixteen seventeen eighteen" \
				 "nineteen".split()
	tens = "twenty thirty forty fifty sixty seventy eighty ninety".split()
	def words(n):
		if n < 20:
			return to19[n-1:n] #when n==0 return ""
		if n < 100:
			return [tens[n//10-2]] + words(n%10)
		if n < 1000:
			return [to19[n//100-1]] + ["hundred"] + words(n%100)
		for p, w in enumerate(("thousand", "million", "billion"), 1):
			if n < 1000**(p+1):
				return words(n//1000**p) + [w] + words(n%1000**p)
	return " ".join(words(num)) or "zero"

def numToWords(num):
	LESS_THAN_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve",
									"Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
	TENS = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
	THOUSANDS = ["", "Thousand", "Million", "Billion"]

	def helper(num):
		if (num == 0):
			return ""
		elif num < 20:
			return LESS_THAN_20[num] + " "
		elif num < 100:
			return TENS[num // 10] + " " + helper(num % 10)
		else:
			return LESS_THAN_20[num // 100] + " Hundred " + helper(num % 100)

	if num == 0: return "Zero"
	i = 0
	words = ""
	while num > 0:
		if num % 1000 != 0:
			words = helper(num % 1000) + THOUSANDS[i] + " " + words
			num //= 1000
			i += 1
	return words.strip()


print(num_to_english(123))
print(num_to_english(12345))
print(num_to_english(1234567))

print(numToWords(123))