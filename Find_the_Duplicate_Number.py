# -*- coding:utf-8 -*-


import sys

class Solution(object):
	def findDuplicate(self, nums):
		n = len(nums)
		ans = 0
		for i in range(32):
			mask = 1 << i
			a = b = 0
			for j in range(n):
				a += (j & mask)
				b += (nums[j] & mask)
			ans += (mask if b > a else 0)

		return ans


if __name__ == "__main__":
	s = Solution()
	nums = [1,2,3,4,5,6,6,6,6,7]
	print s.findDuplicate(nums)
