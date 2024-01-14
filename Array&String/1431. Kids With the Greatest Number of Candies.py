# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        
        kid_max = max(candies)
        
        # For-loop version
        result = []
        for i in range(len(candies)):
            if candies[i] + extraCandies >= kid_max:
                result.append(True)
            else: 
                result.append(False)

        return result

        # List comprehension version
        return [True if candies[i] + extraCandies >= kid_max else False for i in range(len(candies))]