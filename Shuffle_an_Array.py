# -*- coding:utf-8 -*-
#
#        Author : TangHanYi
#        E-mail : thydeyx@163.com
#   Create Date : 2016-11-24 11:37:19 PM
# Last modified : 2016-11-24 11:37:34 PM
#     File Name : Shuffle_an_Array.py
#          Desc :

class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type size: int
        """
        self.initial = nums[:]
        self.nums = nums
        self.n = len(nums)
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.initial
        

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        n = self.n
        nums = self.nums[:]
        while n != 0:
            pos = int(random.random() * n)
            nums[pos], nums[n - 1] = nums[n - 1], nums[pos]
            n -= 1
            
        return nums

if __name__ == "__main__":
	s = Solution()
