# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/?envType=study-plan-v2&envId=leetcode-75

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set("aeiou")
        count = 0

        for char in s[0:k]:
            if char in vowels:
                count += 1

        maxvow = count

        for i in range(k, len(s)):
            count += (s[i] in vowels) - (s[i-k] in vowels)
            maxvow = max(maxvow, count)

        return maxvow

