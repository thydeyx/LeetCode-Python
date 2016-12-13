# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-12 05:19:31 PM
# Last modified : 2016-12-13 02:44:30 PM
#     File Name : Number_of_Islands.py
#          Desc :
class Solution(object):
	
	def findIsland(self, i, j):
		
		self.visited[i][j] = True
		for d in range(4):
			x = i + self.dirX[d]
			y = j + self.dirY[d]
			if x < 0 or x >= self.n or y < 0 or y >= self.m or self.visited[x][y] == True or self.grid[x][y] == '0':
				continue
			self.findIsland(x, y)


	def numIslands(self, grid):
		self.grid = grid
		n = len(grid)
		if n == 0:
			return 0
		m = len(grid[0])
		if m == 0:
			return 0
		self.n = n
		self.m = m
		self.visited = []
		self.dirX = [-1, 0, 1, 0]
		self.dirY = [0, -1, 0, 1]
		ret = 0

		for i in range(n):
			self.visited.append([False for i in range(m)])

		for i in range(n):
			for j in range(m):
				if self.visited[i][j] == False and self.grid[i][j] == '1':
					self.findIsland(i, j)
					ret += 1

		return ret 
		

if __name__ == "__main__":
	s = Solution()
	grid = ["11110","11010","11000","00000"]
	print s.numIslands(grid)
