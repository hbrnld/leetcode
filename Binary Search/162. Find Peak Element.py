# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 1

        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[-1] > nums[-2]:
            return len(nums)-1
        
        while i < len(nums)-1:
            while nums[i] < nums[i+1]:
                i += 1
            return i
        
    def findPeakElementFast(self, nums):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
        