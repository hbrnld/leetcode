# https://leetcode.com/problems/trapping-rain-water/description/?envType=company&envId=goldman-sachs&favoriteSlug=goldman-sachs-thirty-days

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0

        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        volume = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    volume += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    volume += right_max - height[right]
                right -= 1
        
        return volume