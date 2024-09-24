# https://leetcode.com/problems/search-suggestions-system/?envType=study-plan-v2&envId=leetcode-75

import bisect

class Solution(object):
    def suggestedProducts(self, products, searchWord):
        """
        :type products: List[str]
        :type searchWord: str
        :rtype: List[List[str]]
        """

        # Bisect left returns the index in a sorted list 
        # such that the argument passed can be placed to maintain the sorted order.

        products.sort()
        result = []
        current = ''

        for c in searchWord:
            current += c
            i = bisect.bisect_left(products, current)
            result.append([word for word in products[i:i+3] if word.startswith(current)])
        return result
        