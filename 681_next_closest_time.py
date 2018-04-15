"""
681 Next closest time
http://www.cnblogs.com/grandyang/p/7623614.html

"""

class Solution(object):
	def next_closest_time(self, time):
		if not time:
			return
		tmp = time
		tmp = tmp.replace(":", "")
		time_list = list(time)
		nums = "".join(sorted(tmp))
		for i in range(len(time_list))[::-1]:
			if time[i] == ":":
				continue
			pos = nums.find(time_list[i])
			if pos == len(nums)-1:
				time_list[i] = nums[0]
			else:
				next = nums[pos+1]
				if (i == 4 or
					(i == 3 and next <= "5") or
					(i == 1 and (time_list[0] < "2" or time_list[0] == "2" and next <= "3")) or
					(i == 0 and next <= "2")):
					time_list[i] = next
					return "".join(time_list)
				time_list[i] = nums[0]
		return "".join(time_list)

s = Solution()
print s.next_closest_time("19:34") #10:39
print s.next_closest_time("23:59") #22:22