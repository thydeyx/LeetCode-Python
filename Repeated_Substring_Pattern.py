# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-21 05:13:40 PM
# Last modified : 2016-11-21 05:31:40 PM
#     File Name : Repeated_Substring_Pattern.py
#          Desc :
class Solution(object):
	def repeatedSubstringPattern(self, string):
		s = '$' + string
		j = 0
		n = len(s)
		P = [0 for i in range(n)]
		for i in range(2, n):
			while j > 0 and s[i] != s[j + 1]:
				j = P[j]
			if s[i] == s[j + 1]:
				j += 1
			P[i] = j

		n -= 1
		return P[n] and (n % (n - P[n])) == 0


if __name__ == "__main__":
	s = Solution()
	string = 'abcabcabcabc'
	print s.repeatedSubstringPattern(string)
