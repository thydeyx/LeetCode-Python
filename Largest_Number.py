# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-06 06:59:40 PM
# Last modified : 2017-01-06 07:02:13 PM
#     File Name : Largest_Number.py
#          Desc :
"""
通过排序，大小比较为两个字符串拼接后的字典序
"""
class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
		num = [str(x) for x in num]
		num.sort(cmp=lambda x, y: cmp(y+x, x+y))
		return ''.join(num).lstrip('0') or '0'


if __name__ == "__main__":
	s = Solution()
	num = [3, 30, 34, 5, 9]
	print s.largestNumber(num)
