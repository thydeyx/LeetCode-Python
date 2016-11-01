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


	def insert(self, val):
		if self.hashtable.has_key(val) == True:
			return False
		else:
			self.queue.append(val)
			self.hashtable[val] = self.n
			self.n += 1
			return True

	def remove(self, val):
		if self.hashtable.has_key(val) == True:
			position = self.hashtable.get(val, 0)
			self.queue[self.n - 1], self.queue[position] = self.queue[position], self.queue[self.n - 1]
			self.n -= 1
			self.queue.pop()
			return True
		else:
			return False
		

	def getRandom(self):
		i = random.randint(0, self.n - 1)
		ret = self.queue[i]
		return ret


if __name__ == "__main__":
	randomSet = RandomizedSet()
	print randomSet.insert(1);
	print randomSet.remove(2);
	print randomSet.insert(2);
	print randomSet.getRandom();
	print randomSet.remove(1);
	print randomSet.insert(2);
	print randomSet.getRandom();
	
