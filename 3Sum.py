class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        le=len(nums)
        ans=[]
        for i in range(le-2):
            l=i+1
            r=le-1
            while l<r:
                if (nums[l]+nums[r])>-nums[i]:
                    r-=1
                elif (nums[l]+nums[r])<-nums[i]:
                    l+=1
                else:
                    tmp=[nums[i],nums[l],nums[r]]
                    try:
                        ans.index(tmp)
                        r-=1
                        l+=1
                    except:
                        #print(tmp)
                        ans.append(tmp)
                    continue
        return ans
        
