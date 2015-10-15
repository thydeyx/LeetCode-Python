import math,sys
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        le=len(nums)
        ans=0
        m=sys.maxsize
        for i in range(le-2):
            l=i+1
            r=le-1
            #print(i)
            while l<r:
                if abs(nums[l]+nums[r]+nums[i]-target)<m:
                    m=abs(nums[l]+nums[r]+nums[i]-target)
                    ans=nums[l]+nums[r]+nums[i]
                if (nums[l]+nums[r]+nums[i])>target:
                    r-=1
                elif (nums[l]+nums[r]+nums[i])<target:
                    l+=1
                else:
                    r-=1
                    l+=1
        return ans
        
