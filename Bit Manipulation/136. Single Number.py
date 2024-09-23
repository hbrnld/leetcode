# https://leetcode.com/problems/single-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 1. Iterate through the list
        # 2. Update each using XOR - duplicates cancel out
        # 3. Remaining state is binary of unique entry

        c = 0
        for num in nums:
            c = c ^ num
        return c