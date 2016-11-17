# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-17 01:48:52 PM
# Last modified : 2016-11-17 02:30:51 PM
#     File Name : Assign_Cookies.py
#          Desc :
class Solution(object):
	def findContentChildren(self, g, s):
		s = sorted(s, reverse=True)
		g = sorted(g, reverse=True)
		n = len(s)
		l = len(g)
		j = 0
		ret = 0
		for i in range(l):
			if j >= n:
				break

			if s[j] >= g[i]:
				j += 1
				ret += 1
		
		return ret


if __name__ == "__main__":
	s = Solution()
	g = [1, 2, 3]
	s1 = [1, 1]
	print s.findContentChildren(g, s1)
