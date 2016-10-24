# -*- coding:utf-8 -*-

import sys


class Point(object):

	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y


class Solution(object):

	def cross(self, p1, p2):
		return p1.x * p2.y - p2.x * p1.y


	def onSegment(self, p1, p2, p3):
		if cross(p3 - p1, p3 - p2) == 0:
			return True
		return False


	def maxPoints(self, points):
		ret = 0
		dict_x = {}
		for p1 in points:
			dict_k = {}
			maxK = 0
			for p2 in points:
				if p1 == p2:
					continue
				if p1.x != p2.x:
					k = ((p1.y - p2.y) * 1.0) / ((p1.x - p2.x) * 1.0)
					now_k = dict_k.setdefault(k, 1)
					dict_k[k] = now_k + 1
					if now_k + 1 > maxK:
						maxK = now_k + 1
			now_x = dict_x.get(p1.x, 0)
			dict_x[p1.x] = now_x + 1
			if maxK > ret:
				ret = maxK
			if now_x + 1 > ret:
				ret = now_x

		return ret


if __name__ == "__main__":
	s = Solution()
	point1 = Point(1, 1)
	point2 = Point(0, 0)
	point3 = Point(2, 2)
	point4 = Point(1, 2)
	points = [point1, point2, point3, point4]
	print s.maxPoints(points)
