# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-28 16:06:01
#   File Name : Word_Search.py
#        Desc :
import copy

class Solution(object):

	def dfs(self, board, x, y, word, i):

		if i == self.w_l:
			return True

		if x < 0 or y < 0 or x >= self.n or y >= self.m or ord(board[x][y]) != ord(word[i]):
			return False
		
		board[x][y] = chr((ord(board[x][y]) ^ 255))
		ret = self.dfs(board, x + 1, y, word, i + 1) or self.dfs(board, x -1 ,y, word, i + 1) or self.dfs(board, x, y + 1, word, i + 1) or self.dfs(board, x, y - 1, word, i + 1)
		board[x][y] = chr((ord(board[x][y]) ^ 255))
		
		return ret


	def exist(self, board, word):
		self.w_l = len(word)
		if self.w_l < 0:
			return True
		self.n = len(board)
		if self.n == 0:
			return False
		self.m = len(board[0])
		if self.m == 0:
			return False

		for i in range(self.n):
			for j in range(self.m):
				if self.dfs(board, i, j, word, 0) == True:
					return True

		return False


if __name__ == "__main__":
	s = Solution()
	board = [
		['A','B','C','E'],
		['S','F','C','S'],
		['A','D','E','E']
	]
	word = ["ABCCED", "SEE", "ABCB"]
	for w in word:
		print s.exist(board, w)
