# https://leetcode.com/problems/greatest-common-divisor-of-strings/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """

        # Concatenated strings have to be equal
        if str1 + str2 != str2 + str1:
            return ""

        # Find greatest common denominator
        gcd = min(len(str1), len(str2))

        while len(str1) % gcd != 0 or len(str2) % gcd != 0:
            gcd -= 1

        return str1[:gcd]

        