# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 12:05:18 AM
# Last modified : 2016-11-23 12:08:28 AM
#     File Name : Arranging_Coins.py
#          Desc :
class Solution(object):
	def arrangeCoins(self, n):
		m = 1
		while True:
			if m * (m + 1) / 2 > n:
				break
			m += 1
		return m - 1


if __name__ == "__main__":
	s = Solution()
	n = 2100000000
	print s.arrangeCoins(n)
