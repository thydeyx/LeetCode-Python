# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-11 09:33:17 AM
# Last modified : 2016-12-11 10:44:35 AM
#     File Name : Super_Pow.py
#          Desc :


class Solution(object):
	def superPow(self, a, b):
		if len(b) == 0:
			return a
		tmp = a
		ret = 1
		n = len(b)
		k = 0
		while k != n - 1:
			if b[-1] % 2 == 1:
				ret = (ret * tmp) % 1337
			tmp = (tmp * tmp) % 1337
			pre = 0
			for i in range(k, n):
				pre_b = (pre * 10 + b[i]) % 2
				b[i] = (pre * 10 + b[i]) / 2
				pre = pre_b
				if k == i and b[i] == 0:
					k += 1
		return ret


if __name__ == "__main__":
	s = Solution()
	a = 2
	b = [1, 0]
	print s.superPow(a, b)
