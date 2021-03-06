# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-26 21:21:41
#   File Name : First_Missing_Positive.py
#        Desc :
"""
因为这个数不会超过N，所以把每个数交换到本来的位置上,扫描一边就好了
"""
class Solution(object):
	def firstMissingPositive(self, nums):
		n = len(nums)
		if n == 0:
			return 1
		i = 0
		while i < n:
			if (nums[i] <= 0 or nums[i] > n) and i < n:
				i += 1
				continue
			if nums[nums[i] - 1] != nums[i]:
				nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
			else:
				i += 1
		for i in range(n):
			if nums[i] - 1 != i:
				return i + 1
		
		return n + 1
		

if __name__ == "__main__":
	s = Solution()
	nums = [3,4,-1,1]
	print s.firstMissingPositive(nums)
