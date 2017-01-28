# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-28 11:54:33 AM
# Last modified : 2017-01-28 12:16:53 PM
#     File Name : Count_The_Repetitions.py
#          Desc :

class Solution(object):
	def getMaxRepetitions(self, s1, n1, s2, n2):
		if n1 == 0 or n2 == 0:
			return 0
		if s1 == '' or s2 == '':
			return 0
		l1 = len(s1)
		l2 = len(s2)
		j = 0
		repeat = 0
		firstRe = 0
		lastRe = 0
		repeatList = [0 for i in range(n1 + 1)]
		s2Label = [0 for i in range(l2 + 1)]
		i = 0
		while i <= n1:
			i += 1
			for ch in s1:
				if ch == s2[j]:
					j += 1
				if j == l2:
					repeat += 1
					j = 0
			repeatList[i] = repeat
			if j == 0 or s2Label[j] != 0:
				break
			s2Label[j] = i
		if n1 == i:
			return repeatList[n1] / n2
		n1 -= s2Label[j]
		return (n1 / (i - s2Label[j]) * (repeatList[i] - repeatList[s2Label[j]]) + repeatList[n1 % (i - s2Label[j]) + s2Label[j]]) / n2


if __name__ == "__main__":
	s = Solution()
	s1 = 'acb'
	n1 = 4
	s2 = 'ab'
	n2 = 2
	print s.getMaxRepetitions(s1, n1, s2, n2)
