# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = mx = 0
        zero = 1

        while right < len(nums):
            if nums[right] == 0: 
                zero -= 1

            while zero < 0:
                if nums[left] == 0:
                    zero += 1
                left += 1

            mx = max(mx, right-left)
            right += 1

        return mx