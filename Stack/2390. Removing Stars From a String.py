# https://leetcode.com/problems/removing-stars-from-a-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        stack = []

        for char in s: 
            if char != '*':
                stack.append(char)
            else:
                stack.pop()
        
        # Create string from stack
        return ''.join(stack)
        