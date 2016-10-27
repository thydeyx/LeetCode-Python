# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 11:32:10
#   File Name : Jump_Game_II.py
#        Desc :


class Solution(object):
	def jump(self, nums):
		n = len(nums)
		dp = [n + 1 for x in range(n)]
		dp[0] = 0
		for i in range(n):
			for j in range(nums[i]):
				if i + j + 1 < n:
					dp[i + j + 1] = min(dp[i] + 1, dp[i + j + 1])

		return dp[n - 1]


if __name__ == "__main__":
	s1 = Longest_Repeating_Character_Replacement.__file__
	print s1
	s = Solution()
	nums = [2,3,1,1,4]
	print s.jump(nums)
