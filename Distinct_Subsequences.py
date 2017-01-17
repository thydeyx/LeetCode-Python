# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-17 03:47:32 PM
# Last modified : 2017-01-17 04:03:24 PM
#     File Name : Distinct_Subsequences.py
#          Desc :
class Solution(object):
	def numDistinct(self, s, t):
		sl = len(s)
		tl = len(t)
		dp = [[] for i in range(tl + 1)]
		for i in range(tl + 1):
			for j in range(sl + 1):
				if i != 0:
					dp[i].append(0)
				else:
					dp[i].append(1)

		for i in range(1,tl+1):
			for j in range(1,sl + 1):
				if s[j-1] != t[i-1]:
					dp[i][j] = dp[i][j-1]
				else:
					dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

		return dp[tl][sl]


if __name__ == "__main__":
	s = Solution()
	st = 'rabbbit'
	t =	'rabbit'
	print s.numDistinct(st, t)
