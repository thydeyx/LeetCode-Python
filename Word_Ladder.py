# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-09 10:14:54 AM
# Last modified : 2017-01-09 10:50:42 AM
#     File Name : Word_Ladder.py
#          Desc :

import collections
import Queue
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        if wordList == None:
            return 0
        n = len(wordList)
        graph = collections.defaultdict(list)
        dif = 0
        for word1 in wordList:
            for word2 in wordList:
                dif = 0
                m = len(word1)
                for k in range(m):
                    if word1[k] != word2[k]:
                        dif += 1
                        if dif > 1:
                            break
                if dif == 1:
                    graph[word1].append(word2)
        for word in wordList:
            m = len(word)
            dif = 0
            for k in range(m):
                if beginWord[k] != word[k]:
                    dif += 1
                    if dif > 1:
                        break
            if dif == 1 or dif == 0:
                graph['begin$'].append(word)

            dif = 0
            for k in range(m):
                if endWord[k] != word[k]:
                    dif += 1
                    if dif > 1:
                        break
            if dif == 0:
                graph[word].append('end$')
        q = Queue.Queue()
        q.put(('begin$',0))
        visit = {}
        while q.empty() == False:
            now, k = q.get()
            if now == 'end$':
                return k
            for node in graph[now]:
                if visit.has_key(node) == False:
                    visit[node] = 1
                    q.put((node,k + 1))
        return 0

if __name__ == "__main__":
	s = Solution()
	begin = 'hot'
	end = 'dog'
	wordList = set(["hot","dog","dot"])
	print s.ladderLength(begin,end,wordList)
