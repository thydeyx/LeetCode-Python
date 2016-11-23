# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 04:33:03 PM
# Last modified : 2016-11-23 04:52:30 PM
#     File Name : Queue_Reconstruction_by_Height.py
#          Desc :

class Solution(object):

	def compare(self, pair_a, pair_b):
		if pair_a[0] > pair_b[0]:
			return -1
		elif pair_a[0] < pair_b[0]:
			return 1
		elif pair_a[1] > pair_b[1]:
			return 1
		elif pair_a[1] < pair_b[1]:
			return -1
		else:
			return 0


	def reconstructQueue(self, people):
		n = len(people)
		ret = []
		people_height = sorted(people, cmp = self.compare)
		ret.append(people_height[0])
		for i in range(1, n):
			ret.insert(people_height[i][1], people_height[i])
				
		return ret


if __name__ == "__main__":
	s = Solution()
	people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
	print s.reconstructQueue(people)
