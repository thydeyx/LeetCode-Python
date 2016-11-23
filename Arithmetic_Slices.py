# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 09:18:03 PM
# Last modified : 2016-11-23 11:54:53 PM
#     File Name : Arithmetic_Slices.py
#          Desc :
class Solution(object):
	def numberOfArithmeticSlices(self, A):
		addend = 0
		n = len(A)
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
	
