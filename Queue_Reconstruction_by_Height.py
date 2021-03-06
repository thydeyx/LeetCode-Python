# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-23 04:33:03 PM
# Last modified : 2016-11-23 04:59:02 PM
#     File Name : Queue_Reconstruction_by_Height.py
#          Desc :
"""
#we have list of persons represented as [height, key] as input
#First fill the answer list with the tallest persons in ascending order of their keys eg: [7,0], [7,1], [7,2]
#Then fill the next tallest persons in the answer list at index same as key. eg: [7,0],[6,1],[7,1],[7,2],[6,5]
#so on

more explanation:

#First sort the input list in descending order of heights and ascending order of keys
#now iterate over the list and insert each person into answer array at index same as key of person.

eg: input : [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
sort input: [[7,0], [7,1], [6,1], [5,0], [5,2], [4,4]
iterate over sorted array and insert each person at index same as key of the person
answer array grows like this for each iteration.
"""
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
		if n == 0:
			return ret
		people_height = sorted(people, cmp = self.compare)
		ret.append(people_height[0])
		for i in range(1, n):
			ret.insert(people_height[i][1], people_height[i])
				
		return ret


if __name__ == "__main__":
	s = Solution()
	people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
	print s.reconstructQueue(people)
