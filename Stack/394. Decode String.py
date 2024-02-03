# https://leetcode.com/problems/decode-string/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = 0
        stack = []
        output = ''

        for char in s: 
            if char.isdigit(): 
                num = num * 10 + int(char)
            elif char == '[':
                stack.append(num)
                stack.append(output)
                num = 0
                output = ''
            elif char == ']':
                output = stack.pop() + output * stack.pop()
            else: 
                output += char
        
        return output

        