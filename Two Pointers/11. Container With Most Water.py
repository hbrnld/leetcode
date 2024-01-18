# https://leetcode.com/problems/container-with-most-water/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left = 0
        right = len(height)-1

        current_max = 0

        while left < right: 
            area = min(height[left], height[right]) * (right-left)
            if area > current_max: 
                current_max = area
            
            if height[left] > height[right]:
                right -= 1
            else: 
                left += 1

        return current_max