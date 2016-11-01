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

		stack = []
		top = -1
		root = TreeNode(inorder)
		stack.append(root)
		top += 1
		i = 0
		n = len(inorder)

		while top >= 0:
			word = preorder[i]
			i += 1
			node = stack.pop()
			top -= 1
			if len(node.val) == 1:
				node.val = node.val[0]
				node.left = None
				node.right = None
			else:
				k = node.val.index(word)
				leftList = node.val[:k]
				rightList = node.val[k + 1:]
				if len(leftList) == 0:
					left = None
				else:
					left = TreeNode(leftList) 

				if len(rightList) == 0:
					right = None
				else:
					right = TreeNode(rightList)
				
				node.left = left
				node.right = right

				if right != None:
					stack.append(right)
					top += 1

				if left != None:
					stack.append(left)
					top += 1

		root.val = preorder[0]
		self.dfs(root)
		return root


if __name__ == "__main__":
	s = Solution()
	preorder = list("ABDEFC")
	inorder = list("DBEFAC")
	preorder = [1, 2, 3]
	inorder = [2, 1, 3]
	print s.buildTree(preorder, inorder)
	
