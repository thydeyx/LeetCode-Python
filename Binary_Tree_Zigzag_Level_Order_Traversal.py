# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-12-13 05:42:55 PM
# Last modified : 2016-12-14 06:40:58 PM
#     File Name : Binary_Tree_Zigzag_Level_Order_Traversal.py
#          Desc :

import Queue
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
	def zigzagLevelOrder(self, root):
		if root == None:
			return [[]]

		q = Queue.Queue()
		q.put(root)
		ret = []
		k = 0
		while q.empty() != True:
			n = q.qsize()
			i = 0
			tmp = []
			while i < n:
				i += 1
				node = q.get()
				tmp.append(node.val)
				if node.left != None:
					q.put(node.left)
				if node.right != None:
					q.put(node.right)
			if k % 2 == 0:
				ret.append(tmp[:])
			else:
				ret.append(tmp.reverse()[:])
			k += 1
		return ret


if __name__ == "__main__":
	s = Solution()
	root = TreeNode(1)
	print s.zigzagLevelOrder(root)
