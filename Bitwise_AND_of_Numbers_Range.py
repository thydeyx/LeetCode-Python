# -*- coding:utf-8 -*-
"""
如果n的二进制位长度长于m，则对于n所有位置而言，从n到m的数将形成n的位置中的每一种情况，必然有一种情况是n相反的数
如果n，m的二进制位数一样长，则对于二者公共前缀保留，剩下的必然相反
"""
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
