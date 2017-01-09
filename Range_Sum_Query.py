# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2017-01-09 02:32:12 PM
# Last modified : 2017-01-09 02:39:02 PM
#     File Name : Range_Sum_Query.py
#          Desc :

class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        n = len(nums)
        self.n = n
        if n != 0:
            self.bit = [0 for i in range(n + 1)]
            for i in range(n):
                self.update(i,nums[i])
        print self.bit
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: int
        """
        i += 1
        while i <= self.n:
            self.bit[i] += val
            i = i + (i & (-i))
        

    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        j += 1
        ret = 0
        while i > 0:
            ret += self.bit[i]
            i = i - (i & (-i))
        ret1 = 0
        while j > 0:
            ret1 += self.bit[j]
            j = j - (j & (-j))
        return ret1 - ret

if __name__ == "__main__":
	nums = [1, 3, 5]
	s = NumArray(nums)
	print s.sumRange(1,2)
