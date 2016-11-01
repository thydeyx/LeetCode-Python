# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-11-01 15:07:27
#   File Name : Triangle.py
#        Desc :
class Solution(object):
	def minimumTotal(self, triangle):
		n = len(triangle)
		dp = [0 for i in range(n)]
		for i in range(n):
			dp[i] = triangle[n - 1][i]
		for i in range(n-2,-1,-1):
			for j in range(i + 1):
				dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
		
		return dp[0]


if __name__ == "__main__":
	s = Solution()
	triangle = [
		[2],
		[3,4],
		[6,5,7],
		[4,1,8,3]
	]

	print s.minimumTotal(triangle)
