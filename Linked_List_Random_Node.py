# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-07 03:31:51 PM
# Last modified : 2016-11-07 03:52:52 PM
#     File Name : Linked_List_Random_Node.py
#          Desc :

import sys
import random
"""
1/(n+1)
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

	def __init__(self, head):
		self.head = head


	def getRandom(self):
		ret = self.head.val
		p = self.head.next
		n = 1
		while p != None:
			q = int(random.random() * (n + 1))
			if q == 0:
				ret = p.val
			p = p.next
			n += 1
		return ret


if __name__ == "__main__":
	head = ListNode(11)
	p = head

	for i in range(10):
		tmp = ListNode(i)
		p.next = tmp
		p = p.next

	s = Solution(head)
	print s.getRandom()
