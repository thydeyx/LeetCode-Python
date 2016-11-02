# -*- coding:utf-8 -*-
#
#      Author : TangHanYi
#      E-mail : thydeyx@163.com
# Create Date : 16-11-01 17:00:56
#   File Name : Insert_Delete_GetRandom_O1.py
#        Desc :
import random
class RandomizedSet(object):

	def __init__(self):
		self.hashtable = {}
		self.queue = []
		self.n = 0
		self.total = 0


	def insert(self, val):
		self.total += 1
		position, num = self.hashtable.get(val, (-1, -1))
		if position == -1:
			self.queue.append(val)
			self.hashtable[val] = (self.n, 1)
			self.n += 1
		else:
			self.hashtable[val] = (position, num + 1)
			return False
				
		return True


	def remove(self, val):
		if self.hashtable.has_key(val) == True:
			self.total -= 1
			position, num = self.hashtable.get(val, (-1, -1))
			if position == self.n - 1:
				if num == 1:
					self.n -= 1
					del self.hashtable[val]
					self.queue.pop()
					return True
				else:
					num -= 1
					self.hashtable[val] = (position, num)
					return True
			if num == 1:
				del self.hashtable[val]
				tmp, num = self.hashtable.get(self.queue[self.n - 1], (-1, -1))
				self.queue[self.n - 1], self.queue[position] = self.queue[position], self.queue[self.n - 1]
				self.hashtable[self.queue[position]] = (position, num)
				self.n -= 1
				self.queue.pop()
				return True
			else:
				num -= 1
				self.hashtable[val] = (position, num)
				return True
		else:
			return False
		

	def getRandom(self):
		if self.n == 0:
			return None
		i = int(random.random() * self.total) % self.n
		ret = self.queue[i]
		return ret


if __name__ == "__main__":
	randomSet = RandomizedSet()
	print randomSet.getRandom();
	print randomSet.insert(1);
	print randomSet.remove(2);
	print randomSet.insert(2);
	print randomSet.getRandom();
	print randomSet.remove(1);
	print randomSet.insert(2);
	print randomSet.getRandom();
	
