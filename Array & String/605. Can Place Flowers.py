# https://leetcode.com/problems/can-place-flowers/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        for i in range(len(flowerbed)): 
            left = False
            right = False

            # Check if left position free
            if i == 0 or flowerbed[i-1] == 0:
                left = True 

            # Check if right position free
            if i == len(flowerbed)-1:
                right = True
            elif flowerbed[i+1] == 0:
                right = True
            
            # Check if we can place flower, decrease n
            if flowerbed[i] == 0 and left and right: 
                flowerbed[i] = 1
                n -= 1

        return n <= 0       