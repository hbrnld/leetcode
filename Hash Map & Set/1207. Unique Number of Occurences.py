# https://leetcode.com/problems/unique-number-of-occurrences/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        occ = dict()

        for num in arr: 
            if num in occ.keys():
                occ[num] += 1
            else: 
                occ[num] = 1
        
        return len(occ.values()) == len(set(occ.values()))
        