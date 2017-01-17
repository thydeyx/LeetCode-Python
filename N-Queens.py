# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-17 04:35:29 PM
# Last modified : 2017-01-17 04:55:18 PM
#     File Name : N-Queens.py
#          Desc :
import copy
class Solution(object):
	def isVaild(self, state, row, col):
		for i in range(row):
			if state[i] == col or abs(row - i) == abs(col - state[i]):
				return False
		return True


	def helper(self, state, row, ans):
		if row == self.n:
			ret = []
			for l in ans:
				ret.append(''.join(l))
			self.ret.append(ret)
			return

		for col in range(n):
			if self.isVaild(state,row,col):
				state[row] = col
				ans[row][col] = 'G'
				self.helper(state, row + 1, ans)
				ans[row][col] = '.'
				state[row] = -1


	def solveNQueens(self, n):
		self.ret = []
		self.n = n
		state = [-1 for i in range(n)]
		ans = [[] for i in range(n)]
		for i in range(n):
			for j in range(n):
				ans[i].append('.')
		self.helper(state, 0, ans)
		return self.ret

if __name__ == "__main__":
	s = Solution()
	n = 4
	print s.solveNQueens(n)
