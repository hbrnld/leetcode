# https://leetcode.com/problems/edit-distance/?envType=study-plan-v2&envId=leetcode-75

# Problem: Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.
# You have the following three operations permitted on a word:
# Insert a character
# Delete a character
# Replace a character

word1 = "horse"
word2 = "ros"

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        # Create a 2D array
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

        # Fill the first row
        for i in range(len(word1) + 1):
            dp[i][0] = i

        # Fill the first column
        for j in range(len(word2) + 1):
            dp[0][j] = j
        
        # Fill the rest of the array
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                # If the characters are the same, take the diagonal value
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                # If the characters are different, take the minimum of the three values, and add 1
                else:
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        
        # for row in dp:
        #     print(row)

        return dp[-1][-1]
        
s = Solution()
print(s.minDistance(word1, word2))
