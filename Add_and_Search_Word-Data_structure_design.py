# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-07 04:13:43 PM
# Last modified : 2017-01-07 04:16:22 PM
#     File Name : Add_and_Search_Word-Data_structure_design.py
#          Desc :
"""
字典树的另一种用法
for else 语句 当for正常结束时else语句被执行
"""
class WordDictionary(object):
    def __init__(self):
        self.word_dict = collections.defaultdict(list)
        

    def addWord(self, word):
        if word:
            self.word_dict[len(word)].append(word)

    def search(self, word):
        if not word:
            return False
        if '.' not in word:
            return word in self.word_dict[len(word)]
        for v in self.word_dict[len(word)]:
            # match xx.xx.x with yyyyyyy
            for i, ch in enumerate(word):
                if ch != v[i] and ch != '.':
                    break
            else:
                return True
        return False

if __name__ == "__main__":
	s = Solution()
