# -*- coding:utf-8 -*-


import sys


class Solution(object):

	def fullJustify(self, words, maxWidth):

		n = maxWidth
		sentence_list = []
		ret_list = []
		sentence_l = 0
		word_c = 0

		for word in words:
			word_l = len(word)
			word_c += 1
			if sentence_l + word_l + word_c - 1 <= n:
				sentence_l += word_l
				sentence_list.append(word)
			else:
				word_c -= 1
				if word_c > 1:
					space = (n - sentence_l) / (word_c - 1)
					space_surplus = (n - sentence_l) % (word_c - 1)
				s = ""
				if word_c == 1:
					s = s + sentence_list[0] + " " * (n - len(sentence_list[0]))
				else:
					for s_word in sentence_list:
						if word_c > 1:
							s = s + s_word + " " * (space + (lambda x:1 if x > 0 else 0)(space_surplus))
							space_surplus -= 1
						else:
							s = s + s_word
						word_c -= 1

				sentence_l = len(word)
				ret_list.append(s)
				sentence_list = [word]
				word_c = 1

		if word_c > 1:
			space = (n - sentence_l) / (word_c - 1)
			space_surplus = (n - sentence_l) % (word_c - 1)
		s = ""
		for s_word in sentence_list:
			if word_c > 1:
				s = s + s_word + " "
			else:
				s = s + s_word + " " * (n - sentence_l - word_c)
			word_c -= 1

		ret_list.append(s)

		return ret_list				


if __name__ == "__main__":
	s = Solution()
	words = ["This", "is", "an", "example", "of", "text", "justification."]
	maxWidth = 16
	print s.fullJustify(words, maxWidth)
