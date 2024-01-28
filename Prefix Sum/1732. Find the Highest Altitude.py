# https://leetcode.com/problems/find-the-highest-altitude/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        
        current, mx = 0, 0

        for alt in gain:
            current += alt
            if current > mx:
                mx = current

        return mx