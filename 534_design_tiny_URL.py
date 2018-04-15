"""
534 Design tiny URL

https://leetcode.com/problems/encode-and-decode-tinyurl/discuss/100268/Two-solutions-and-thoughts
"""
import random
import string

class Codec:
	urlBase = "https://tinyurl.com/"
	alphabet = string.ascii_letters + "0123456789"
	count = 6

	def __init__(self):
		self.url2code = {}
		self.code2url = {}

	def encode(self, longUrl):
		while longUrl not in self.url2code:
			code = "".join([random.choice(self.alphabet) for _ in range(self.count)])
			if code not in self.code2url:
				self.code2url[code] = longUrl
				self.url2code[longUrl] = code
		return self.urlBase + self.url2code[longUrl]

	def decode(self, shortUrl):
		return self.code2url.get(shortUrl[-self.count:])
