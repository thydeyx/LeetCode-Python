# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-10-28 17:15:43
#   File Name : Construct_Binary_Tree_from_Preorder_and_Inorder_Traversal.py
#        Desc :
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	
	def dfsBulid(self, root, word):
		if root == None:
			return False

		if type(root.val) != list:
			if self.dfsBulid(root.left, word) == True:
				return True
			if self.dfsBulid(root.right, word) == True:
				return True
		elif  root.val == word:
			root.left = None
			root.right = None
			return True

		if word in root.val:
			i = root.val.index(word)
			leftList = root.val[:i]
			rightList = root.val[i + 1:]
			left = None
			right = None
			if len(leftList) == 1:
				leftList = leftList[0]

			if len(rightList) == 1:
				rightList = rightList[0]

			if type(leftList) == list and len(leftList) != 0:
				left = TreeNode(leftList)

			if type(rightList) == list and len(rightList) != 0:
				right = TreeNode(rightList)

			root.val = root.val[i]
			root.left = left
			root.right = right
			return True

		return False


	def dfs(self, root):
		if root == None:
			return

		print root.val
		self.dfs(root.left)
		self.dfs(root.right)
		return 


	def buildTree(self, preorder, inorder):
		if len(preorder) == 0 or len(inorder) == 0:
			return []
		root = TreeNode(inorder)
		for word in preorder:
			self.dfsBulid(root, word)
			print "#######"
		#self.dfs(root)
		return root
						


if __name__ == "__main__":
	s = Solution()
	preorder = list("ABDEFC")
	inorder = list("DBEFAC")
	print s.buildTree(preorder, inorder)
	
