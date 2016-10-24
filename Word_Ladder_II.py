# -*- coding:utf-8 -*- 

import sys
import Queue

class Solution(object):

	def comp(self, now_word, next_word):
		n = len(now_word)
		diff = 0
		for i in range(n):
			if now_word[i] != next_word[i]:
				diff += 1
			if diff > 1:
				return 0

		return 1


	def dfs(self, fromList, i):
		
		node = fromList[i]
		if i == self.n + 1:
			self.tmp.append(self.endWord)
		elif i == 0:
			self.tmp.append(self.beginWord)
			self.tmp.reverse()
			self.ret.append(self.tmp[:])
			self.tmp.reverse()
			self.tmp.pop()
			return
	
		for to in node[1]:
			if i != self.n + 1:
				self.tmp.append(self.wordlist[i - 1])
			self.dfs(fromList, to)
			if i != self.n + 1:
				self.tmp.pop()


	def findLadders(self, beginWord, endWord, wordlist):
		q = Queue.Queue()
		self.ret = []
		self.tmp = []
		self.wordlist = wordlist
		self.beginWord = beginWord
		self.endWord = endWord
		n = len(wordlist)
		self.n = n
		fromList = [[sys.maxint, []] for x in range(n + 2)]
		inQ = [0 for x in range(n + 2)]
		inQ[0] = 1
		fromList[0][0] = 0
		q.put((beginWord, fromList[0], 0))
		while q.empty() == False:
			n = len(wordlist)
			now_word, state, num_word = q.get()
			inQ[num_word] = 0
			if num_word == n + 1:
				continue
			if self.comp(now_word, endWord) == 1:
				if state[0] + 1 < fromList[n + 1][0]:
					fromList[n + 1][0] = state[0] + 1
					fromList[n + 1][1] = [num_word]
					if inQ[n + 1] == 0:
						q.put((endWord, fromList[n + 1], n + 1))
						inQ[n + 1] = 1
				elif state[0] + 1 == fromList[n + 1][0]:
					fromList[n + 1][1].append(num_word)
					if inQ[n + 1] == 0:
						q.put((endWord, fromList[n + 1], n + 1))
						inQ[n + 1] = 1
			for i in range(n):
				if self.comp(now_word, wordlist[i]) == 1:
					if state[0] + 1 < fromList[i + 1][0]:
						fromList[i + 1][0] = state[0] + 1
						fromList[i + 1][1] = [num_word]
						if inQ[i + 1] == 0:
							q.put((wordlist[i], fromList[i + 1], i + 1))
							wordlist.remove(wordlist[i])
							inQ[i + 1] = 1
					elif state[0] + 1 == fromList[i + 1][0]:
						fromList[i + 1][1].append(num_word)
						if inQ[n + 1] == 0:
							q.put((endWord, fromList[n + 1], i + 1))
							wordlist.remove(wordlist[i])
							inQ[n + 1] = 1

		if fromList[n + 1][0] != sys.maxint:
			self.dfs(fromList, n + 1)
		return self.ret


if __name__ == "__main__":
	s = Solution()
	beginWord = "hit"
	endWord = "cog"
	wordList = ["hot","dot","dog","lot","log"]
	print s.findLadders(beginWord, endWord, wordList)
