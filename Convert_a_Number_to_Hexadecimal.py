# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-21 04:35:06 PM
# Last modified : 2016-11-21 04:51:12 PM
#     File Name : Convert_a_Number_to_Hexadecimal.py
#          Desc :
class Solution(object):
	def toHex(self, num):
		if num == 0:
			return "0"
		hexList = []
		tmp = 0
		hexDict = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
		for i in range(33):
			if i % 4 == 0 and i != 0:
				hexList.append(tmp)
				tmp = 0
			if (num & (1 << i)) != 0:
				tmp = tmp | 1 << (i % 4)

		hexList = hexList[::-1]
		ret = []
		begin = 0
		for i in hexList:
			if i != 0:
				break
			begin += 1

		for i in range(begin, 8):
			if hexList[i] < 10:
				ret.append(str(hexList[i]))
			else:
				ret.append(hexDict[hexList[i]])
		return ''.join(ret)


if __name__ == "__main__":
	s = Solution()
	num = -1
	print s.toHex(num)
