# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        first = second = float('inf')

        for third in nums: 
            if third <= first: 
                first = third
            elif third <= second: 
                second = third
            else:                   # Found number such that first < second < third
                return True
            
        return False