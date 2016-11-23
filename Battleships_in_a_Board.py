# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 05:03:30 PM
# Last modified : 2016-11-23 05:14:40 PM
#     File Name : Battleships_in_a_Board.py
#          Desc :
class Solution(object):
	def countBattleships(self, board):
		n = len(board)
		if n == 0:
			return 0
		m = len(board[0])
		ret = 0

		for i in range(n):
			for j in range(m):
				if board[i][j] != '.' and ((i - 1 < 0 and (j - 1 < 0 or board[i][j - 1] != 'X')) or (j - 1 < 0 and (i - 1 < 0 or board[i - 1][j] != 'X'))):
					ret += 1
					continue
				if board[i][j] == '.' or board[i-1][j] == 'X' or board[i][j-1] == 'X':
					continue
				ret += 1

		return ret


if __name__ == "__main__":
	s = Solution()
	board = ["X..X","...X","...X"]
	print s.countBattleships(board)
