# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-05 01:01:26 PM
# Last modified : 2017-01-05 02:25:58 PM
#     File Name : Evaluate_Reverse_Polish_Notation.py
#          Desc :


class Solution(object):
	def evalRPN(self, tokens):
		n = len(tokens)
		if n == 1:
			return int(tokens[0])
		num_stack = []
		#num_stack.append(tokens[0])
		#num_stack.append(tokens[1])
		for i in range(n):
			if tokens[i] == '/':
				b = int(num_stack.pop()) 
				a = int(num_stack.pop())
				tmp = a / b
				num_stack.append(tmp)
				print a,b,num_stack[-1],'/'
			elif tokens[i] == '*':
				b = int(num_stack.pop()) 
				a = int(num_stack.pop())
				tmp = a * b
				num_stack.append(tmp)
				print num_stack[-1],'*'
			elif tokens[i] == '-':
				b = int(num_stack.pop()) 
				a = int(num_stack.pop())
				tmp = a - b
				num_stack.append(tmp)
				print num_stack[-1],'-'
			elif tokens[i] == '+':
				b = int(num_stack.pop()) 
				a = int(num_stack.pop())
				tmp = a + b
				num_stack.append(tmp)
				print num_stack[-1],'+'
			else:
				num_stack.append(tokens[i])
		return num_stack[0]


if __name__ == "__main__":
	s = Solution()
	#tokens = ["2", "1", "+", "3", "*"]
	tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
	print s.evalRPN(tokens)
