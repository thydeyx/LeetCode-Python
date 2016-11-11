# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-11 01:11:23 PM
# Last modified : 2016-11-11 01:59:31 PM
#     File Name : Find_All_Numbers_Disappeared_in_an_Array.py
#          Desc :
"""
循环移动
"""
class Solution(object):
	def findDisappearedNumbers(self, nums):
		n = len(nums)
		ret = []
		for i in range(n):
			index = abs(nums[i]) - 1
			if nums[index] < 0:
				ret.append(index + 1)
			
			nums[index] = - nums[index]

		return ret


if __name__ == "__main__":
	s = Solution()
	nums = [4,3,2,7,8,2,3,1]
	print s.findDisappearedNumbers(nums)
