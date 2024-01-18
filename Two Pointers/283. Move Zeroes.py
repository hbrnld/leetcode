# https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i, j = 0, 0

        while i < n and j < n: 
            if nums[i] != 0: # Find the first zero
                i += 1
            
            if nums[j] == 0: # Find the first non-zero
                j += 1
            
            if i < j and j < n:
                nums[i], nums[j] = nums[j], nums[i]

            j += 1