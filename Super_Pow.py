# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-11 09:33:17 AM
# Last modified : 2016-12-11 09:50:10 AM
#     File Name : Super_Pow.py
#          Desc :


class Solution(object):
	def superPow(self, a, b):
		if len(b) == 0:
			return a
		tmp = a
		ret = 1
		n = len(b)
		while sum(b) != 0:
			if b[-1] % 2 == 1:
				ret = (ret * tmp) % 1337
			tmp = (tmp * tmp) % 1337
			pre = 0
			for i in range(n):
				pre_b = (pre * 10 + b[i]) % 2
				b[i] = (pre * 10 + b[i]) / 2
				pre = pre_b
		return ret


if __name__ == "__main__":
	s = Solution()
	a = 2
	b = [1, 0]
	print s.superPow(a, b)
