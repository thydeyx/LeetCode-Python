# -*- coding:utf-8 -*-


import sys

class Solution(object):
	def getMoneyAmount(self, n):
		dp = [[0] * (n+1) for _ in range(n+ 1)]
		for gap in range(1, n):
			for low in range(1, n + 1 - gap):
				high = low + gap
				dp[low][high] = min(x + max(dp[low][x-1], dp[x+1][high])for x in range(low, high))

		return dp[1][n]


if __name__ == "__main__":
	s = Solution()
	n = 10
	print s.getMoneyAmount(n)
