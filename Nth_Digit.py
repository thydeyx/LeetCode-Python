# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-21 08:29:47 PM
# Last modified : 2016-11-21 10:59:50 PM
#     File Name : Nth_Digit.py
#          Desc :
class Solution(object):
	def findNthDigit(self, n):
		tmp = 9
		base = 9
		begin = 1
		i = 1
		while tmp < n:
			tmp = tmp + base * 10 * (i + 1)
			i += 1
			base *= 10
			begin *= 10

		tmp = tmp - base * i
		n = n - tmp
		ge = n / i
		y = n % i
		if y == 0:
			ge -= 1
			begin += ge
			return begin  % 10
		else:
			begin += ge
			y = i - y
			while y != 0:
				begin /= 10
				y -= 1
			return begin % 10
		

if __name__ == "__main__":
	s = Solution()
	n = 21
	print s.findNthDigit(n)
