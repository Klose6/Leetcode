"""
Radix Sort
https://en.wikipedia.org/wiki/Radix_sort#Example_in_Python
"""

class RadixSort(object):
	def list_to_buckets(self, array, base, iteration):
		buckets =[[] for _ in range(base)]
		for num in array:
			digit = (num//base**iteration) % base
			buckets[digit].append(num)
		return buckets
	def bucket_to_list(self, buckets):
		res = []
		for buc in buckets:
			for num in buc:
				res.append(num)
		return res
	def radix_sort(self, array, base=10):
		maxval = max(array)
		it=0
		while base ** it <= maxval:
			array = self.bucket_to_list(self.list_to_buckets(array, base, it))
			it+=1
		return array

s=RadixSort()
print s.radix_sort([1,2,36,26,32])