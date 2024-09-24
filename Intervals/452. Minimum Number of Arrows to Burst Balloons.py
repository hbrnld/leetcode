# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

# Input: points = [[10,16],[2,8],[1,6],[7,12]]
# Output: 2
# Explanation: The balloons can be burst by 2 arrows

class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        
        points.sort(key=lambda x: x[0])
        right = points[0][1]
        count = 1
        
        for balloon in points[1:]:
            if balloon[0] > right: 
                count += 1  
                right = balloon[1] 
            else:
                right = min(right, balloon[1])
        
        return count