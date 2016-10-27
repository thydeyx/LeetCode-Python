# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 11:32:10
#   File Name : Jump_Game_II.py
#        Desc :
"""
设置两个边界，如果i遍历超过了当前的边界，则步数需要增加，下个边界通过当前边界内能到达的点去扩充，这样最后求出的就是最小步数
"""
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
