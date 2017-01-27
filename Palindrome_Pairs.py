# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-27 10:43:36 AM
# Last modified : 2017-01-27 11:06:08 AM
#     File Name : Palindrome_Pairs.py
#          Desc :

class Trie:
	def __init__(self, x):
		self.val = x
		self.child = [None for i in range(26)]

class Solution(object):
	def createTrie(self, words, root):
		p = None
		for i in range(len(words)):
			word = words[i]
			p = root
			for w in word:
				num = ord(w) - ord('a')
				if p.child[num] == None:
					p.child[num] = Trie('#')
				p = p.child[num]
			p.val = i


	def palindromePairs(self, words):
		root = Trie('#')
		self.createTrie(words, root)
		ret = []
		n = len(words)
		for i in range(n):
			p = root
			word = words[i][::-1]
			k = 0
			l = len(word)
			for k in range(l):
				#print k, '$' * 20
				num = ord(word[k]) - ord('a')
				if p.child[num] != None:
					p = p.child[num]
				else:
					break
				#print word[k], p.val
			try:
				target = int(p.val)
				if k == l-1:
					ret.append([i, target])
			except Exception as e:
				continue
		return ret


if __name__ == "__main__":
	s = Solution()
	words = ["bat", "tab", "cat"]
	print s.palindromePairs(words)
