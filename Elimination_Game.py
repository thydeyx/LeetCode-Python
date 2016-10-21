# -*- coding:utf-8 -*-
class Solution(object):
	def __init__(self):
		self.left = True
		self.step = 1
		self.head = 1
		

	def lastRemaining(self, n):
		while n != 1:
			if self.left == True:
				self.left = False
				self.head += self.step
				self.step *= 2
				n = n / 2
			else:
				self.left = True
				if n % 2 != 0:
					self.head += self.step
				self.step *= 2
				n = n / 2
		return self.head
		
		

if __name__ == "__main__":
	s = Solution()
	n = 9
	print s.lastRemaining(n)
