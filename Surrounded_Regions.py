# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-17 09:03:13 PM
# Last modified : 2016-11-17 09:59:15 PM
#     File Name : Surrounded_Regions.py
#          Desc :
import Queue
class Solution(object):
	def solve(self, board):
		n = len(board)
		if n == 0:
			return board
		m = len(board[0])

		visited = [[] for i in range(n)]
		for i in range(n):
			for j in range(m):
				visited[i].append(0)

		stack = []
		q = Queue.Queue()
		xa = [1, 0, -1, 0]
		ya = [0, 1, 0, -1]
		for i in range(n):
			for j in range(m):
				if board[i][j] == 'O' and visited[i][j] == 0:
					visited[i][j] = 1
					flag = True
					q.put((i, j))
					stack = []
					stack.append((i, j))
					if i == 0 or j == 0 or i == n - 1 or j == m - 1:
						flag = False
					while q.empty() == False:
						y,x = q.get()
						for k in range(4):
							if x + xa[k] < m and x + xa[k] >= 0 and y + ya[k] < n and y + ya[k] >=0 and visited[y + ya[k]][x + xa[k]] == 0:
								visited[y + ya[k]][x + xa[k]] = 1
								if board[y + ya[k]][x + xa[k]] == 'O':
									q.put((y + ya[k], x + xa[k]))
									stack.append((y + ya[k], x + xa[k]))
									if x + xa[k] == 0 or x + xa[k] == m - 1 or y + ya[k] == 0 or y + ya[k] == n - 1:
										flag = False
					if flag == True:
						for y, x in stack:
							tmp = list(board[y])
							tmp[x] = 'X'
							board[y] = ''.join(tmp)

		return board


if __name__ == "__main__":
	s = Solution()
	board = ["XXXX","XOOX","XXOX","XOXX"]
	s.solve(board)
	print board
