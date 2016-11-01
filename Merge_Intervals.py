# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-11-01 16:09:18
#   File Name : Merge_Intervals.py
#        Desc :
import sys
import operator

class Solution(object):

	def cmp_me(self, x, y):
		if x[0] < y[0]:
			return -1
		elif x[0] > y[0]:
			return 1
		else:
			if x[1] < y[1]:
				return -1
			elif x[1] > y[1]:
				return 1
			else:
				return 0


	def merge(self, intervals):
		#print sorted(intervals, key=operator.itemgetter(1), reverse=True)
		intervals = sorted(intervals, cmp=self.cmp_me)
		n = len(intervals)
		pre = intervals[0]
		ret = []
		for i in range(1, n):
			if intervals[i][0] <= pre[1]:
				pre[1] = intervals[i][1]
			else:
				ret.append(pre[:])
				pre = intervals[i]
		ret.append(pre[:])
		return ret

if __name__ == "__main__":
	s = Solution()
	intervals = [[1,3],[2,6],[2,5],[8,10],[15,18]]
	print s.merge(intervals)
