# https://leetcode.com/problems/max-number-of-k-sum-pairs/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        nums.sort()
        ops, left, right = 0, 0, len(nums)-1

        while left < right: 
            s = nums[left] + nums[right] 
            if s < k:
                left += 1 
            elif s > k: 
                right -= 1
            else: 
                ops += 1
                left += 1
                right -= 1
        return ops

    def maxOperationsCounter(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from Collections import Counter

        ops, counter = 0, Counter(nums)
        
        for value, cnt in counter.items(): 
            diff = k - value     # Find matching value that sums to k

            if diff in counter and diff <= value: 
                if value != diff:
                    ops += min(cnt, counter[diff])
                else: 
                    ops += cnt // 2
        
        return ops