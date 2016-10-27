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
		dp = [ False for x in range(n)]
		dp[0] = True
		for i in range(n):
			if dp[i] == True:
				for j in range(nums[i]):
					if i + j + 1 >= n:
						break
					dp[i +j + 1] = True
		return dp[n - 1]


if __name__ == "__main__":
	s = Solution()
	nums = [2,3,1,1,4]
	nums = [3,2,1,0,4]
	print s.canJump(nums)
