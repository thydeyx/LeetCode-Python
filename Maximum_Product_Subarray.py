# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-11-01 15:53:47
#   File Name : Maximum_Product_Subarray.py
#        Desc :
class Solution(object):
	def maxProduct(self, nums):
		n = len(nums)
		maxpre = nums[0]
		minpre = nums[0]
		maxret = nums[0]
		for i in range(1, n):
			maxnow = max(nums[i], max(nums[i] * maxpre, nums[i] * minpre))
			minnow = min(nums[i], min(nums[i] * maxpre, nums[i] * minpre))
			maxret = max(maxnow, maxret)
			maxpre = maxnow
			minpre = minnow
		
		return maxret


if __name__ == "__main__":
	s = Solution()
	nums = [2,3,-2,4]
	print s.maxProduct(nums)
