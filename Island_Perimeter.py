# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-20 10:29:19 PM
# Last modified : 2016-11-20 11:01:17 PM
#     File Name : Island_Perimeter.py
#          Desc :
import Queue
class Solution(object):
	def islandPerimeter(self, grid):
		n = len(grid)
		if n == 0:
			return 0
		m = len(grid[0])
		g = [[] for i in range(n)]
		for i in range(n):
			for j in range(m):
				g[i].append(0)

		ret = 0
		q = Queue.Queue()
		xa = [0, 1, 0, -1]
		ya = [1, 0, -1, 0]
		for i in range(n):
			for j in range(m):
				if grid[i][j] == 1:
					q.put((i, j))
					g[i][j] = 1
					break
			if q.empty() == False:
				break
		
		while q.empty() == False:
			x, y = q.get()
			for k in range(4):
				i = x + xa[k]
				j = y + ya[k]
				if i >= 0 and i < n and j >= 0 and j < m and grid[i][j] == 1 and g[i][j] == 0:
					g[i][j] = 1
					q.put((i, j))
				if i == -1 or i == n or j == -1 or j == m or grid[i][j] == 0:
					ret += 1
		return ret


if __name__ == "__main__":
	s = Solution()
	grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
	print s.islandPerimeter(grid)
