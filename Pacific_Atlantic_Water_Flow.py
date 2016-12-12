# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-12 03:59:52 PM
# Last modified : 2016-12-12 04:50:09 PM
#     File Name : Pacific_Atlantic_Water_Flow.py
#          Desc :
import Queue
class Solution(object):

	def findPath(self, q, ret, matrix, n, m):
		
		#q = Queue.Queue()
		dirX = [-1, 0, 1, 0]
		dirY = [0, -1, 0, 1]
		#q.put((i,j))
		#ret[i][j] = True
		while q.empty() == False:
			x, y = q.get()
			for d in range(4):
				x_step = x + dirX[d]
				y_step = y + dirY[d]
				if x_step < 0 or x_step >= n or y_step < 0 or y_step >= m or ret[x_step][y_step] == True or matrix[x_step][y_step] < matrix[x][y]:
					continue
				ret[x_step][y_step] = True
				q.put((x_step, y_step))


	def pacificAtlantic(self, matrix):
		
		ret = []

		n = len(matrix)
		if n == 0:
			return ret
		m = len(matrix[0])
		if m == 0:
			return ret
		Pacific = []
		Atlantic = []
		pQueue = Queue.Queue()
		aQueue = Queue.Queue()
		for i in range(n):
			Pacific.append([False for j in range(m)]) 
			Atlantic.append([False for j in range(m)])

		for i in range(n):
			pQueue.put(i, 0)
			q.Queue.put(i, m - 1)
			Pacific[i][0] = True
			Atlantic[i][m - 1] = True
			#self.findPath(i, 0, Pacific, matrix, n, m)
			#self.findPath(i, m - 1, Atlantic, matrix, n, m)

		for i in range(m):
			pQueue.put(0, i)
			q.Queue.put(n - 1, i)
			Pacific[0][i] = True
			Atlantic[n - 1][i] = True
			#self.findPath(0, i, Pacific, matrix, n, m)
			#self.findPath(n - 1, i, Atlantic, matrix, n, m)
		self.findPath(pQueue, Pacific, matrix, n, m)
		self.findPath(aQueue, Pacific, matrix, n, m)

		for i in range(n):
			for j in range(m):
				if Pacific[i][j] == True and Atlantic[i][j] == True:
					ret.append([i,j])

		return ret


if __name__ == "__main__":
	s = Solution()
	matrix = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
	print s.pacificAtlantic(matrix)
