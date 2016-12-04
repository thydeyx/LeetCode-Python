# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-04 11:45:58 AM
# Last modified : 2016-12-04 12:12:45 PM
#     File Name : Longest_Repeating_Character_Replacement.py
#          Desc :
class Solution(object):
	def characterReplacement(self, s, k):
		l = len(s)
		start = 0
		ret = 0
		max_word = 0
		word_count = [0 for i in range(26)]
		
		for end in range(l):
			word_count[ord(s[end]) - ord('A')] += 1
			max_word = max(max_word, word_count[ord(s[end]) - ord('A')])
			while end - start + 1 - max_word > k:
				word_count[ord(s[start]) - ord('A')] -= 1
				start += 1

			ret = max(ret, end - start + 1)

		return ret


if __name__ == "__main__":
	s = Solution()
	st = "AABABBA"
	k = 1
	print s.characterReplacement(st, k)	
