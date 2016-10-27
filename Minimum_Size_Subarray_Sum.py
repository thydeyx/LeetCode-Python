# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 09:15:38
#   File Name : Minimum_Size_Subarray_Sum.py
#        Desc :

class Solution(object):
	def minSubArrayLen(self, s, nums):
		n = len(nums)
		ret = n + 1
		i = 0
		count = 0
		for j in range(n):
			count += nums[j]
			while i <= j and count >= s:
				ret = min(ret, j - i + 1)
				count -= nums[i]
				i += 1
		if ret == n + 1:
			return 0
		else:
			return ret


if __name__ == "__main__":
	s = Solution()
	q = 7
	nums = [2,3,1,2,4,3]
	print s.minSubArrayLen(q, nums)
