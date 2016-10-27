# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 11:32:10
#   File Name : Jump_Game_II.py
#        Desc :


class Solution(object):
	def jump(self, nums):
		n = len(nums)
		currentBoundry = 0
		nextBoundry = 0
		step = 0
		for i in range(n):
			if i > currentBoundry:
				currentBoundry = nextBoundry
				step += 1
			if i + nums[i] > nextBoundry:
				nextBoundry = i + nums[i]

		return step


if __name__ == "__main__":
	s = Solution()
	nums = [2,3,1,1,4]
	print s.jump(nums)
