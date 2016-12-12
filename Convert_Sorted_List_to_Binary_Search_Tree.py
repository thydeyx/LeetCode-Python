# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-12 02:41:52 PM
# Last modified : 2016-12-12 03:51:22 PM
#     File Name : Convert_Sorted_List_to_Binary_Search_Tree.py
#          Desc :
# Definition for singly-linked list.
import sys
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

	def inorderHelper(self, s, e):
		
		if s > e:
			return None
		mid = s + (e - s) / 2
		
		left = self.inorderHelper(s, mid - 1)
		root = TreeNode(self.node.val)
		root.left = left
		self.node = self.node.next

		right = self.inorderHelper(mid + 1, e)
		root.right = right
		return root


	def sortedListToBST(self, head):
		if head == None:
			return None

		p = head
		self.node = head
		n = 0
		while p.next != None:
			n += 1
			p = p.next
		
		return self.inorderHelper(0, n)
		

if __name__ == "__main__":
	s = Solution()
	i = 1
	head = ListNode(i)
	p = head
	while i < 20:
		i += 1
		tmp = ListNode(i)
		p.next = tmp
		p = p.next

	s.sortedListToBST(head)
