# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-28 15:28:11
#   File Name : Unique_Paths_II.py
#        Desc :
class Solution(object):
	def uniquePathsWithObstacles(self, obstacleGrid):
		n = len(obstacleGrid)
		m = len(obstacleGrid[0])
		dp = [[0 for i in range(m)] for j in range(n)]
		print dp
		dp[0][0] = 1
		for i in range(n):
			for j in range(m):
				if obstacleGrid[i][j] != 1:
					if i > 0 and obstacleGrid[i - 1][j] != 1:
						dp[i][j] += dp[i - 1][j]
					if j > 0 and obstacleGrid[i][j - 1] != 1:
						dp[i][j] += dp[i][j - 1]
		
		return dp[n - 1][m - 1]


if __name__ == "__main__":
	s = Solution()
	obstacleGrid = [
		[0,0,0],
	    [0,1,0],
		[0,0,0]
	]
	print s.uniquePathsWithObstacles(obstacleGrid)
