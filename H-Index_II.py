# -*- coding:utf-8 -*-

"""
二分查找注意边界条件
"""
class Solution(object):
	def hIndex(self, citations):
		"""
		:type citations: List[int]
		:rtype: int
		"""
		l = 0
		r = len(citations) - 1
		n = r + 1
		if n == 0:
			return 0

		while l < r:
			mid = (l+r)/2
			if citations[mid] >= n - mid:
				r = mid
			elif citations[mid] < n - mid:
				l = mid + 1

		if citations[n - 1] < 1:
			return 0

		return n - r
