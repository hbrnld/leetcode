# https://leetcode.com/problems/unique-paths/?envType=study-plan-v2&envId=leetcode-75

from math import comb

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # Create a 2D array to store the number of unique paths
        dp = [[1 for _ in range(n)] for _ in range(m)]

        # Fill array with sum of previous states
        for i in range(1, m):   
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

        return dp[-1][-1]
    
    def uniquePathsMath(self, m, n):
        # Total m+n-2 steps, down-steps can be placed anywhere
        # Number of ways to place is (n choose k)
        
        total_steps = m + n - 2
        down_steps = m - 1
        
        return comb(total_steps, down_steps)
