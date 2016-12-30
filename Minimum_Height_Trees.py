# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-30 03:45:13 PM
# Last modified : 2016-12-30 03:55:57 PM
#     File Name : Minimum_Height_Trees.py
#          Desc :

import copy
import Queue
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        q = Queue.Queue()
        tmq = Queue.Queue()
        degree = [0 for i in range(n)]
        flag = [0 for i in range(n)]
        graph = [[] for i in range(n)]
        m = 0
        
        if n == 2:
            return edges[0]
            
        for edge in edges:
            degree[edge[0]] += 1
            degree[edge[1]] += 1
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        for i in range(n):
            if degree[i] == 1:
                q.put(i)
                flag[i] = 1
                degree[i] -= 1
        while n - m > 2:
            while q.empty() == False:
                node = q.get()
            
                for adj in graph[node]:
                    degree[adj] -= 1
                    if degree[adj] == 1:
                        tmq.put(adj)
                m += 1
            if n - m <= 2:
                break
            while tmq.empty() == False:
                j = tmq.get()
                q.put(j)
                flag[j] = 1
            
        ret = []
        for i in range(n):
            if flag[i] == 0:
                ret.append(i)
        return ret
	
	

if __name__ == "__main__":
	s = Solution()
	n = 6
	r = [[0,1],[0,2],[0,3],[3,4],[4,5]]
	print s.findMinHeightTrees(n, r)
