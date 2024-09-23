# https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

text1 = "abcde"
text2 = "ace"

class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m, n = len(text1), len(text2)
        
        # Create a 2D array to store the length of the longest common subsequence
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        # Fill the dp array using bottom-up dynamic programming
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Result is stored in the bottom-right cell of the dp array
        return dp[m][n]