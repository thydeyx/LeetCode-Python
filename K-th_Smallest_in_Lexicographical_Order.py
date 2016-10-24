# -*- coding:utf-8 -*-

import sys

class Solution(object):
	def findKthNumber(self, n, k):
		ret = 1
		k -= 1
		while k > 0:
			count = 0
			interval = [ret, ret + 1]
			while interval[0] <= n:
				count += min(interval[1], n + 1) - interval[0]
				interval = [10 * interval[0], 10 * interval[1]]
		
			if count <= k:
				k -= count
				ret = ret + 1
			else:
				k -= 1
				ret = ret * 10

		return ret


if __name__ == "__main__":
	s = Solution()
	n = 13
	k = 2
	print s.findKthNumber(n, k)
