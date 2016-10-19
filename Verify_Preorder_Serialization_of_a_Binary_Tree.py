#! -*- coding:utf-8 -*-
import sys
"""
通过非递归的前序遍历，构造出二叉树，通过判断相关条件得到
非递归前序遍历过程，首先构造根节点，压入栈内，不断出栈，如果出栈元素
左子树为空则挂到左子树上，并将两个节点前后压入栈中，
如果左子树不为空，则将节点挂到右子树上，将新节点入栈，
如果遇到#则持续出栈，不作处理，完毕
"""
class Tnode(object):
	def __init__(self, data):
		self.right = None
		self.left = None
		self.data = data
	

	def __str__(self):
		return self.data

class Solution(object):
	def dfs(self, root):
		if root.left != None:
			self.dfs(root.left)
		if root.right != None:
			self.dfs(root.right)


	def isValidSerialization(self, preorder):
		preorder_list = preorder.split(',')
		n = len(preorder_list)
		stack_list = []
		top = -1
		i = -1
		root = None
		first = True
		self.flag = True
		#dfs(preorder_list)
		while i < n - 1:
			i += 1
			node_data = preorder_list[i]
			if first:
				first = False
				node = Tnode(node_data)
				root = node
				stack_list.append(node)
				top += 1
			else:
				if top >= 0:
					father_node = stack_list.pop()
					top -= 1
					if father_node.data == '#':
						i -= 1
						continue
					elif father_node.left == None:
						
						node = Tnode(node_data)
						father_node.left = node
						stack_list.append(father_node)
						top += 1
						stack_list.append(node)
						top += 1
					elif father_node.left != None:
						node = Tnode(node_data)
						father_node.right = node
						stack_list.append(node)
						top += 1
				else:
					self.flag = False

		if len(stack_list) != 1 or stack_list[0].data != '#':
			self.flag = False

		return self.flag
		
					
if __name__ == "__main__":
	s = Solution()
	preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
	print s.isValidSerialization(preorder)
	
	
	
