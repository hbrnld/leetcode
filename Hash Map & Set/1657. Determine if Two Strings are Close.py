# https://leetcode.com/problems/determine-if-two-strings-are-close/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        d1 = []
        d2 = []
        
        # Compare lengths and chars
        if len(word1) != len(word2) or set(word1) != set(word2):
            return False

        # Slower solution
        # from collections import Counter
        # d1 = Counter(word1)
        # d2 = Counter(word2)

        for ch in set(word1):
            d1.append(word1.count(ch))
            d2.append(word2.count(ch))

        if sorted(d1) == sorted(d2):
            return True
        return False
            
        
    
