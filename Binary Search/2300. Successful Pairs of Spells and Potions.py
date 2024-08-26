# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/?envType=study-plan-v2&envId=leetcode-75

from bisect import bisect_left

def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        pairs = []

        potions.sort()
        for spell in spells:
            need = (success + spell - 1) // spell   # ceil(success/spell)
            index = bisect_left(potions, need)
            pairs.append(len(potions) - index)
        return pairs