# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-03 04:56:59 PM
# Last modified : 2016-12-03 05:35:05 PM
#     File Name : Partition_Equal_Subset_Sum.py
#          Desc :
class Solution(object):
	def canPartition(self, nums):
		s = sum(nums)
		if (s & 1) != 0:
			return False

		to_dict = {0:0}
		for i in nums:
			for key in to_dict.keys():
				to_dict[key + i] = 0
				if key + i == (s >> 1):
					return True


if __name__ == "__main__":
	s = Solution()
	nums = [1, 5, 11, 5]
	nums =  [1, 2, 3, 5]
	print s.canPartition(nums)
