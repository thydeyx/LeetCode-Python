# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-24 11:39:42 PM
# Last modified : 2016-11-24 11:59:09 PM
#     File Name : Is_Subsequence.py
#          Desc :
"""
class Solution(object):
	def isSubsequence(self, s, t):
		s = '$' + s
		t = '$' + t
		sn = len(s)
		tn = len(t)
		P = [0 for i in range(sn)]
		j = 0
		for i in range(2, sn):
			while j > 0 and s[i] != s[j + 1]:
				j = P[j]
			if s[i] == s[j + 1]:
				j += 1
			P[i] = j
		
		j = 0
		for i in range(1, tn):
			while j > 0 and t[i] != s[j + 1]:
				j = P[j]
			if t[i] == s[j + 1]:
				j += 1
			if j == sn - 1:
				print i - sn + 1
				j = P[j]

		return False
"""

class Solution(object):
	def isSubsequence(self, s, t):
		sn = len(s)
		tn = len(t)
		if sn == 0:
			return True

		j = 0
		for i in range(tn):
			if t[i] == s[j]:
				j += 1
			if j == sn:
				return True

		return False


if __name__ == "__main__":
	s = Solution()
	st = "abc"
	t = "diejfabcldjfabc"
	print s.isSubsequence(st, t)
