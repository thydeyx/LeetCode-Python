# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-27 05:05:37 PM
# Last modified : 2016-12-27 05:18:32 PM
#     File Name : Repeated_DNA_Sequences.py
#          Desc :

class Solution(object):
	def findRepeatedDnaSequences(self, s):
		w_dict = {}
		ret = []
		n = len(s)
		for i in range(n - 9):
			hash_key = 0
			for j in range(10):
				hash_key = ((ord(s[i + j]) & 7) << (j * 3)) | hash_key 
			if w_dict.has_key(hash_key):
				if w_dict[hash_key] == 1:
					ret.append(s[i:i + 10])
					w_dict[hash_key] += 1
			else:
				w_dict[hash_key] = 1

		return ret
			

if __name__ == "__main__":
	s = Solution()
	st = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
	print s.findRepeatedDnaSequences(st)
