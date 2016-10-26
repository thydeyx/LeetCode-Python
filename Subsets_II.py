# -*- coding:utf-8 -*-


import sys

class Solution(object):
	def dfs(self, nums, cur, tmp):
		if cur == self.n:
			return

		i = cur
		while i < self.n:
			tmp.append(nums[i])
			self.ret.append(tmp[:])
			self.dfs(nums, i + 1, tmp)
			tmp.pop()

			while i < self.n - 1 and nums[i] == nums[i + 1]:
				i += 1
			i += 1

		return


	def subsetsWithDup(self, nums):
		nums = sorted(nums)
		self.ret = [[]]
		self.n = len(nums)
		if self.n == 0:
			return []
		tmp = []
		self.dfs(nums, 0, tmp)

		return self.ret
		


if __name__ == "__main__":
	s = Solution()
	nums = [1,2,2]
	print s.subsetsWithDup(nums)
