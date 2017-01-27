# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-27 10:43:36 AM
# Last modified : 2017-01-27 01:28:06 PM
#     File Name : Palindrome_Pairs.py
#          Desc :

class Trie:
	def __init__(self, x):
		self.val = x
		self.child = [None for i in range(26)]

class Solution(object):
	def isPalindrome(self, word):
		i = 0
		j = len(word) - 1
		while i < j:
			if word[i] != word[j]:
				return False
			i += 1
			j -= 1
		return True


	def palindromePairs(self, words):
		ret = []
		if words == None or len(words) < 2:
			return ret
		n = len(words)
		dict_words = {}
		for i in range(n):
			dict_words[words[i]] = i
		for i in range(n):
			for j in range(len(words[i]) + 1):
				str1 = words[i][:j]
				str2 = words[i][j:]
				if self.isPalindrome(str1) == True:
					str3 = str2[::-1]
					if dict_words.has_key(str3) == True and dict_words[str3] != i:
						ret.append([dict_words[str3],i])
				if self.isPalindrome(str2) == True:
					str3 = str1[::-1]
					if dict_words.has_key(str3) == True and dict_words[str3] != i and len(str2) != 0:
						ret.append([i, dict_words[str3]])
		return ret
	


if __name__ == "__main__":
	s = Solution()
	words = ["a",""]
	print s.palindromePairs(words)
