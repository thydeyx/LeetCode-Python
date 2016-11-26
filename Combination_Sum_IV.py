# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-26 11:34:16 PM
# Last modified : 2016-11-27 12:23:50 AM
#     File Name : Combination_Sum_IV.py
#          Desc :
class Solution(object):
	def combinationSum4(self, nums, target):
		dp = [0 for i in range(target + 1)]
		dp[0] = 1
		n = len(nums)
		for i in range(target + 1):
			for j in range(n):
				if i >= nums[j]:
					dp[i] = dp[i] + dp[i - nums[j]]

		return dp[target]


if __name__ == "__main__":
	s = Solution()
	nums = [1, 2, 3]
	target = 4
	print s.combinationSum4(nums, target)
