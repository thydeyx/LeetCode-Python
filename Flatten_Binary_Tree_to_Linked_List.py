# -*- coding:utf-8 -*-

import sys

class TreeNode(object):
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Solution(object):
	def __init__(self):
		self.pre = None


	def flatten(self, root):
		if root == None:
			return
		self.flatten(root.right)
		self.flatten(root.left)
		
		root.right = self.pre
		root.left = None
		self.pre = root


if __name__ == "__main__":
	s = Solution()
	root = TreeNode(1)
	s.flatten(root)
