# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-15 10:14:10 PM
# Last modified : 2016-11-15 10:21:15 PM
#     File Name : Sum_of_Two_Integers.py
#          Desc :
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
                
        while b != 0:
            x = a ^ b
            y = (a & b) << 1
            a = x
            b = y;
            
        return a


if __name__ == "__main__":
	s = Solution()
	s.getSum(-14, 16)
