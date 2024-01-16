# https://leetcode.com/problems/product-of-array-except-self/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prod = 1

        # If 2 or more zeros
        if nums.count(0) >= 2:
            return [0]*len(nums)

        # If 1 zero
        elif nums.count(0) == 1: 
            zi = nums.index(0)
            for i in range(len(nums)):
                if i != zi:
                    prod *= nums[i]

            output = [0]*len(nums)
            output[zi] = prod
            return output

        # No zeros
        else: 
            output = []
            for i in range(len(nums)):
                prod *= nums[i]
            for i in range(len(nums)):
                output.append(prod / nums[i])

            return output
        