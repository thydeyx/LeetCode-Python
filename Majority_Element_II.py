# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-27 20:37:48
#   File Name : Majority_Element_II.py
#        Desc :
class Solution(object):
	def majorityElement(self, nums):
		n = len(nums)
		ret = []
		if n == 0:
			return ret
		
		number0, number1 = nums[0], nums[1]
		count0, count1 = 1, 1
		for i in range(2, n):
			if count0 == 0:
				number0 = nums[i]
				count0 = 1
			elif count1 == 0:
				number1 = nums[i]
				count1 = 1
			elif nums[i] == number0:
				count0 += 1
			elif nums[i] == number1:
				count1 += 1
			else:
				count0 -= 1
				count1 -= 1

		count0 = 0
		count1 = 0
		for i in range(n):
			if nums[i] == number1:
				count1 += 1
			elif nums[i] == number0:
				count0 += 1

		if count0 > n/3:
			ret.append(number0)
		if count1 > n/3:
			ret.append(number1)
		return ret


if __name__ == "__main__":
	s = Solution()
	nums = [1,1,1,2,2,2,2,3,3,3,3]
	print s.majorityElement(nums)
