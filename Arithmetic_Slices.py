# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 09:18:03 PM
# Last modified : 2016-11-23 11:59:08 PM
#     File Name : Arithmetic_Slices.py
#          Desc :
"""
数组    等差数列的数目    与上一数组的等差数列数目比较
1 2 3			 1     1 - 0 = 1
1 2 3 4			 3     3 - 1 = 2
1 2 3 4 5		 6     6 - 3 = 3
1 2 3 4 5 6		 10    10 - 6 = 4
1 2 3 4 5 6 7    15    15 - 10 = 5
"""
class Solution(object):
	def numberOfArithmeticSlices(self, A):
		addend = 0
		n = len(A)
		if n < 3:
			return 0
		ret = 0
		cha = A[1] - A[0]
		for i in range(2, n):
			if A[i] - A[i - 1] == cha:
				addend += 1
				ret += addend
			else:
				addend = 0

		return ret


if __name__ == "__main__":
	s = Solution()
	A = [1, 2, 3, 4]
	print s.numberOfArithmeticSlices(A)
	
