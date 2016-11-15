# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-15 02:37:43 PM
# Last modified : 2016-11-15 02:50:29 PM
#     File Name : Lexicographical_Numbers.py
#          Desc :
"""
先序遍历
"""
class Solution(object):

	def __init__(self):
		self.ret = []


	def dfs(self, cur):
		if cur > self.n:
			return

		self.ret.append(cur)
		for i in range(10):
			if cur * 10 + i > self.n:
				return
			self.dfs(cur * 10 + i)

		return


	def lexicalOrder(self, n):
		self.n = n

		for i in range(1, 10):
			self.dfs(i)

		return self.ret


if __name__ == "__main__":
	s = Solution()
	n = 14959
	print s.lexicalOrder(n)
