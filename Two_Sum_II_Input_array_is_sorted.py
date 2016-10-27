# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 09:04:15
#   File Name : Two_Sum_II_Input_array_is_sorted.py
#        Desc :
"""
查找l，r时可通过二分查找改进效率
"""
class Solution(object):
	def twoSum(self, numbers, target):
		r = len(numbers) - 1
		l = 0
		while l < r:
			if numbers[l] + numbers[r] < target:
				l += 1
			elif numbers[l] + numbers[r] > target:
				r -= 1
			else:
				return [l+1, r+1]


if __name__ == "__main__":
	s = Solution()
	numbers = [2,7,11,15]
	target = 9
	print s.twoSum(numbers, target)
