# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-07 10:58:56 PM
# Last modified : 2016-12-09 10:21:27 PM
#     File Name : House_Robber_II.py
#          Desc :
class Solution(object):
	def rob(self, nums):
		n = len(nums)
		if n == 0:
			return 0
		if n == 1:
			return nums[1]
		dp = [[0,0] for i in range(n)]
		#dp[0][1] = nums[0]
		for i in range(1, n):
			dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
			dp[i][1] = max(dp[i - 1][0], dp[i][1]) + nums[i]

		ret1 = max(dp[n - 1][0], dp[n - 1][1])
		dp = [[0,0] for i in range(n)]
		dp[0][1] = nums[0]
		dp[1][0] = nums[0]
		for i in range(2, n):
			dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
			dp[i][1] = max(dp[i - 1][0], dp[i][1]) + nums[i]
		return max(ret1, dp[n - 1][0])


if __name__ == "__main__":
	s = Solution()
	nums = [1,2,3,4,5,6]
	print s.rob(nums)
