# https://leetcode.com/problems/house-robber/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)

        if n <= 2: 
            return max(nums)

        dp = [nums[0], nums[1], nums[0] + nums[2]]

        for i in range(3, n):
            dp.append(nums[i] + max(dp[i - 2], dp[i - 3]))
        
        return max(dp[-1], dp[-2])