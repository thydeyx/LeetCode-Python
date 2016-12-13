# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-13 02:47:07 PM
# Last modified : 2016-12-13 05:16:40 PM
#     File Name : Insertion_Sort_List.py
#          Desc :


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
	def insertionSortList(self, head):
		ret = ListNode(head.val)
		while head.next != None:
			head = head.next
			tmp = ret
			pre = ret
			i = 0
			while tmp != None and head.val > tmp.val:
				if i == 0:
					i += 1
				else:
					pre = pre.next
				tmp = tmp.next

			if tmp == ret:
				inode = ListNode(head.val)
				inode.next = tmp
				ret = inode
				continue
			
			if tmp == None:
				inode = ListNode(head.val)
				pre.next = inode
				continue

			inode = ListNode(head.val)
			pre.next = inode
			inode.next = tmp
		return ret


if __name__ == "__main__":
	s = Solution()
	head = ListNode(9)
	p = head
	i = 20
	while i > 0:
		tmp = ListNode(i)
		p.next = tmp
		p = p.next
		i -= 1

	h = s.insertionSortList(head)
	i = 1
	while h != None:
		print h.val
		h = h.next
		i += 1
		if i > 20:
			break

