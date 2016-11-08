# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-08 10:12:47 AM
# Last modified : 2016-11-08 10:45:05 AM
#     File Name : Path_Sum_III.py
#          Desc :
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
	
	def pathRoot(self, root, s):
		if root == None:
			return 0
		
		ret = 0
		if root.val == s:
			ret += 1
		ret = ret + self.pathRoot(root.left, s - root.val) + self.pathRoot(root.right, s - root.val)
		return ret
		

	def pathSum(self, root, s):
		if root == None:
			return 0

		ret = self.pathRoot(root, s) + self.pathSum(root.right, s) + self.pathSum(root.left, s) 
		return ret


if __name__ == "__main__":
	s = Solution()
	root = TreeNode(10)
	root.right = TreeNode(-3)
	r = root.right
	r.right = TreeNode(11)
	root.left = TreeNode(5)
	print s.pathSum(root, 8)
