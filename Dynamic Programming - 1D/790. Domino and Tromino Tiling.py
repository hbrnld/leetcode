# https://leetcode.com/problems/domino-and-tromino-tiling/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def numTilings(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [1,1,2] + [0] * (n-1)

        for i in range(3, n+1):
            dp[i] = dp[i-1] * 2 + dp[i-3]
        
        return dp[n] % (10**9 + 7)
        