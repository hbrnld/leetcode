# https://leetcode.com/problems/n-th-tribonacci-number/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """

        tribs = [0, 1, 1]
        i = 3

        while i <= n:
            tribs.append(sum(tribs[i-3:i]))
            i += 1

        return tribs[n]
        