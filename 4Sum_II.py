# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-04 12:30:49 AM
# Last modified : 2016-12-04 12:38:25 AM
#     File Name : 4Sum_II.py
#          Desc :
import collections
class Solution(object):
	def fourSumCount(self, A, B, C, D):
		AB = collections.Counter(a + b for a in A for b in B)
		return sum([AB[-c-d] for c in C for d in D])


if __name__ == "__main__":
	s = Solution()
	A = [ 1, 2]
	B = [-2,-1]
	C = [-1, 2]
	D = [ 0, 2]
	print s.fourSumCount(A, B, C, D)

