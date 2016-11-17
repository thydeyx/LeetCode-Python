# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-17 01:48:52 PM
# Last modified : 2016-11-17 01:55:23 PM
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
		for i in range(n):
			if j >= l:
				break

			if s[i] > g[j]:
				j += 1
				ret += 1
			else:
				break
		
		return ret

if __name__ == "__main__":
	s = Solution()
	g = [1, 2]
	s1 = [1, 2, 3]
	print s.findContentChildren(g, s1)
