# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # Finite-State Machine
        # s0 represents no position, s1 a long position

        s0 = [0 for _ in range(len(prices))]
        s1 = [0 for _ in range(len(prices))]

        # Base Case
        s0[0] = 0
        s1[0] = -prices[0]

        for i in range(1, len(prices)):
            s0[i] = max(s0[i-1], s1[i-1] + prices[i] - fee)     # Remain no position, or sell
            s1[i] = max(s1[i-1], s0[i-1] - prices[i])           # Remain long position, or buy
        
        return s0[-1]