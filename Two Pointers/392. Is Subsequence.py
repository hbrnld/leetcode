# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i, j = 0, 0

        if not s: 
            return True

        if len(s)>len(t): 
            return False

        while j <= len(t)-1:
            if s[i] == t[j]:
                i += 1
            j += 1

            if i == len(s):
                return True
        
        return False