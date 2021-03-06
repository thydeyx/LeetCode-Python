# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-11-01 16:09:18
#   File Name : Merge_Intervals.py
#        Desc :
import sys
import operator
"""
线段树题目，但目前使用了排序解决
"""
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution(object):

	def cmp_me(self, x, y):
		if x.start < y.start:
			return -1
		elif x.start > y.start:
			return 1
		else:
			if x.end < y.end:
				return -1
			elif x.end > y.end:
				return 1
			else:
				return 0


	def merge(self, intervals):
		#print sorted(intervals, key=operator.itemgetter(1), reverse=True)
		intervals = sorted(intervals, cmp=self.cmp_me)
		n = len(intervals)
		ret = []
		if n == 0:
			return ret
		pre = intervals[0]
		for i in range(1, n):
			if intervals[i].start <= pre.end:
				pre.end = max(pre.end, intervals[i].end)
			else:
				ret.append(pre)
				pre = intervals[i]
		ret.append(pre)
		return ret


if __name__ == "__main__":
	s = Solution()
	intervals = [[1,3],[2,6],[2,5],[8,10],[15,18]]
	tmp = []
	for i in intervals:
		a = Interval(i[0], i[1])
		tmp.append(a)
	intervals = tmp
	r = s.merge(intervals)
	for i in r:
		print i.start, i.end
