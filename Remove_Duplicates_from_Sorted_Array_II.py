
class Solution(object):
	def removeDuplicates(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		if n == 0:
			return n
		j = 1
		c = 1
		pre = nums[0]
		for i in range(1, n):
			if pre != nums[i]:
				pre = nums[i]
				c = 1
				nums[j] = pre
				j += 1
			else:
				c += 1
				if c <= 2:
					c += 1
					nums[j] = pre
					j += 1
		
		return j
	
	 

if __name__ == "__main__":
	s = Solution()
	nums = [1,1,1,2,2,3]
	print s.removeDuplicates(nums)
