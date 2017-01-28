# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-28 09:00:00 PM
# Last modified : 2017-01-28 09:18:42 PM
#     File Name : Interleaving_String.py
#          Desc :

class Solution(object):
	def isInterleave(self, s1, s2, s3):
		l1 = len(s1)
		l2 = len(s2)
		l3 = len(s3)
		if l3 != l1 + l2:
			return False
		dp = [[0 for j in range(l2 + 1)] for i in range(l1 + 1)]
		for i in range(l1 + 1):
			for j in range(l2 + 1):
				if i == 0 and j == 0:
					dp[i][j] = True
				elif i == 0:
					dp[i][j] = (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
				elif j == 0:
					dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1])	
				else:
					dp[i][j] = ((dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]))
		return dp[l1][l2]


if __name__ == "__main__":
	s = Solution()
	s1 = 'aabcc'
	s2 = 'dbbca'
	s3 = 'aadbbcbcac'
	print s.isInterleave(s1, s2, s3)
