# https://leetcode.com/problems/combination-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75

from itertools import combinations

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """

        return [c for c in combinations(range(1, 10), k) if sum(c) == n]
            
    def combinationSum3Recursive(self, k, n):
        def combs(k, n):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, 10)
                    for comb in combs(k-1, n-last, last)]
        return combs(k, n)