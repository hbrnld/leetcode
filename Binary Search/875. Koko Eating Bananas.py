# https://leetcode.com/problems/koko-eating-bananas/description/?envType=study-plan-v2&envId=leetcode-75

'''
There are n piles of bananas, the i:th pile has piles[i] bananas. The guards have gone and will come back in h hours.
We want to find the smallest integer k bananas per hour so that we can finish the work in h hours.

piles = [3,6,7,11], h = 8
Output: 4
'''

import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        low, high = 1, max(piles)

        while low <= high:
            k = (low + high) // 2
            if sum(math.ceil(1.0 * pile / k) for pile in piles) > h:        # Time taken to eat all piles of bananas
                low = k + 1
            else:
                high = k - 1
        return low
        