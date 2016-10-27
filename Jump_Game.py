# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 09:55:41
#   File Name : Jump_Game.py
#        Desc :
class Solution(object):
	def canJump(self, nums):
		n = len(nums)
		i = 0
		reach = 0
		while i <= reach and i < n:
			reach = max(i + nums[i], reach)
			i += 1
		return i == n
		


if __name__ == "__main__":
	s = Solution()
	nums = [2,3,1,1,4]
	nums = [3,2,1,0,4]
	print s.canJump(nums)
