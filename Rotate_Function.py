# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 10:44:17 AM
# Last modified : 2016-11-23 11:27:31 AM
#     File Name : Rotate_Function.py
#          Desc :
"""
第一遍获取到和sum_A
每次移动的增加值为sum_A - A[i] * n
因为每个数增加一倍，最后一个数减少下标乘以A[i]倍
"""
class Solution(object):
	def maxRotateFunction(self, A):
		n = len(A)
		sum_A = sum(A)
		f = 0
		for i, j in enumerate(A):
			f += i * j
		max_f = f
		
		i = n - 1
		while i >= 0:
			f += (sum_A - A[i] * n)
			i -= 1
			max_f = max(max_f, f)
		return max_f


if __name__ == "__main__":
	s = Solution()
	A = [4, 3, 2, 6]
	print s.maxRotateFunction(A)
