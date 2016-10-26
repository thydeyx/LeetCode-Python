# -*- coding:utf-8 -*-


import sys

class Solution(object):
	def rangeBitwiseAnd(self, m, n):
		q = 1
		while m != n:
			m >>= 1
			n >>= 1
			q <<= 1
		return m * q


if __name__ == "__main__":
	s = Solution()
	m = 5
	n = 7
	print s.rangeBitwiseAnd(m, n)
