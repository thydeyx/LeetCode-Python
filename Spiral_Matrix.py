# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 09:33:51
#   File Name : Spiral_Matrix.py
#        Desc :
"""
分四个方向，每次枚举到最后一个数的前一个数，作为下一个方向的开始
"""
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        M = matrix[:]  # duplicate matrix
        m = len(M)  # get m
        n = len(M[0])  # get n
        i, j = 0, 0  # set coordinate
        l = m * n
        k = 0
        res = []
        while k < l:
            # right
            while j < n and M[i][j] is not None:
                res.append(M[i][j])
                M[i][j] = None
                k += 1
                j += 1
            j -= 1
            i += 1
            # down
            while i < m and M[i][j] is not None:
                res.append(M[i][j])
                M[i][j] = None
                k += 1
                i += 1
            i -= 1
            j -= 1
            # left
            while j >= 0 and M[i][j] is not None:
                res.append(M[i][j])
                M[i][j] = None
                k += 1
                j -= 1
            j += 1
            i -= 1
            # up
            while i >= 0 and M[i][j] is not None:
                res.append(M[i][j])
                M[i][j] = None
                k += 1
                i -= 1
            i += 1
            j += 1
        return res


if __name__ == "__main__":
	s = Solution()
	matrix = [
		[ 1, 2, 3 ],
		[ 4, 5, 6 ],
		[ 7, 8, 9 ]
	]
	print s.spiralOrder(matrix)
