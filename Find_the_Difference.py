# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-17 02:34:59 PM
# Last modified : 2016-11-17 02:47:47 PM
#     File Name : Find_the_Difference.py
#          Desc :
class Solution(object):
	def findTheDifference(self, s, t):
		sMap = 0
		tMap = 0
		for letter in s:
			pos = ord(letter) - ord('a')
			sMap = sMap ^ (1 << pos)

		for letter in t:
			pos = ord(letter) - ord('a')
			tMap = tMap ^ (1 << pos)

		tmp = sMap ^ tMap
		ret = 0
		while tmp != 0:
			ret += 1
			tmp >>= 1

		return chr(ret + ord('a') - 1)


if __name__ == "__main__":
	s = Solution()
	s1 = 'abcda'
	t = 'bcdaae'
	print s.findTheDifference(s1, t)

