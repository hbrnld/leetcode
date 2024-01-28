# https://leetcode.com/problems/find-pivot-index/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = right = 0

        for num in nums:
            right += num

        for i, num in enumerate(nums):
            right -= num
            if left == right:
                return i
            left += num

        return -1
        