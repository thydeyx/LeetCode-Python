# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-26 20:27:38
#   File Name : Search_for_a_Range.py
#        Desc :


class Solution(object):
	def searchRange(self, nums, target):
		l = 0
		n = len(nums) - 1
		r = n
		
		while l < r:
			mid = (l + r) / 2
			if nums[mid] == target:
				r = mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1
		retR = r
		
		l = 0
		r = n
		while l < r - 1:
			mid = (l + r) / 2
			if nums[mid] == target:
				l = mid
			elif nums[mid] < target:
				l = mid + 1
			else:
				r = mid - 1
		retL = l
			
		return [retR, retL]


if __name__ == "__main__":
	s = Solution()
	nums = [5, 7, 7, 8, 8, 10]
	target = 8
	print s.searchRange(nums, target)
	