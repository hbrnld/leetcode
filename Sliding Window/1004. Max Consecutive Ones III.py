# https://leetcode.com/problems/max-consecutive-ones-iii/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def longestOnes(self, nums, k):
        left = right = zeros = 0
        mx = -10e9

        while right < len(nums):
            
            if nums[right] == 0:
                zeros += 1

            # While too many zeros (more than k), increment left tail
            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            mx = max(mx, right-left+1)
            right += 1
        
        return mx
        
