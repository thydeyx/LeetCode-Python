# -*- coding:utf-8 -*-

class Solution(object):
	def wiggleMaxLength(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		n = len(nums)
		ret = 0
		dp = [[1,1] for x in range(n)]
		for i in range(n):
			for j in range(i):
				if nums[i] - nums[j] > 0:
					dp[i][0] = max(dp[j][1] + 1, dp[i][0])
				elif nums[i] - nums[j] < 0:
					dp[i][1] = max(dp[j][0] + 1, dp[i][1])

			ret = max(ret, max(dp[i][0], dp[i][1]))

		return ret

if __name__ == "__main__":
	s = Solution()
	nums = [1,7,4,9,2,5]
	print s.wiggleMaxLength(nums)
