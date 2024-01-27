# https://leetcode.com/problems/maximum-average-subarray-i/description/?envType=study-plan-v2&envId=leetcode-75
# Note: Approach using sliding window is faster than list indexing

class Solution:
    def findMaxAverage(self, nums, k):
        
        if k == 1:
            return max(nums)

        currentMax = currentSum = sum(nums[:k])

        for i in range(k, len(nums)):
            currentSum += nums[i] - nums[i-k]
            currentMax = max(currentMax, currentSum)

        return currentMax / k