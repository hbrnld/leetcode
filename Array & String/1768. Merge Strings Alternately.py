# https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def mergeAlternately(self, word1, word2):
        ml = max(len(word1), len(word2))
        result = []
        i = 0

        while i < ml:
            if i < len(word1):
                result.append(word1[i])
            if i < len(word2):
                result.append(word2[i])
            i += 1

        return "".join(result)
        