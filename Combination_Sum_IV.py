# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-26 11:34:16 PM
# Last modified : 2016-11-26 11:39:00 PM
#     File Name : Combination_Sum_IV.py
#          Desc :
class Solution(object):
	def __init__(self):
		self.ret = 0

	def dfs(self, nums, target, n):
		if target == 0:
			self.ret += 1
			return

		for i in range(n):
			if target >= nums[i]:
				self.dfs(nums, target - nums[i], n)


	def combinationSum4(self, nums, target):
		self.dfs(nums, target, len(nums))
		return self.ret


if __name__ == "__main__":
	s = Solution()
	nums = [1, 2, 3]
	target = 4
	print s.combinationSum4(nums, target)
