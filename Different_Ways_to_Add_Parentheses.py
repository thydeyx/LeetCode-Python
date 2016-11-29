# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-30 12:16:30 AM
# Last modified : 2016-11-30 12:29:35 AM
#     File Name : Different_Ways_to_Add_Parentheses.py
#          Desc :
import operator as op
class Solution(object):
	def dfs(self, s):
		if s in self.mem:
			return self.mem[s]
		elif s.isdigit():
			return [int(s)]
		else:
			res = []
			ops = None
			for i in range(len(s)):
				if s[i].isdigit():
					continue
				a1 = self.dfs(s[0:i])
				a2 = self.dfs(s[i+1:])
				if s[i] == '-':
					ops = op.sub
				elif s[i] == '+':
					ops = op.add
				elif s[i] == '*':
					ops = op.mul
				for e1 in a1:
					for e2 in a2:
						res.append(ops(e1, e2))
			self.mem[s] = res
			return res


	def diffWaysToCompute(self, in_put):
		self.mem = {}
		return self.dfs(in_put)


if __name__ == "__main__":
	s = Solution()
	in_put = "2*3-4*5"
	print s.diffWaysToCompute(in_put)
