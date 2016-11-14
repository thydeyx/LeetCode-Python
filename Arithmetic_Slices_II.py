# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-14 02:41:51 PM
# Last modified : 2016-11-14 02:46:10 PM
#     File Name : Arithmetic_Slices_II.py
#          Desc :
class Solution(object):
	def numberOfArithmeticSlices(self, A):
		ret = 0
		n = len(A)
		dp = [{} for x in range(n)]
		for i in range(1, n):
			for j in range(0, i):
				dist = A[i] - A[j]
				s = dp[j].get(dist, 0) + 1
				dp[i][dist] = dp[i].get(dist, 0) + s
				ret += (s - 1)

		return ret


if __name__ == "__main__":
	s = Solution()
	A = [2,4,6,8,10]
	print s.numberOfArithmeticSlices(A)
