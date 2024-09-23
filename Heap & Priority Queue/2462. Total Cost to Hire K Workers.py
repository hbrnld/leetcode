# https://leetcode.com/problems/total-cost-to-hire-k-workers/?envType=study-plan-v2&envId=leetcode-75

import heapq

class Solution(object):
    def totalCost(self, costs, k, candidates):
        """
        :type costs: List[int]
        :type k: int
        :type candidates: int
        :rtype: int
        """

        left, right = 0, len(costs)-1
        total_cost = 0
        pq1, pq2 = [], []

        while k:
            while len(pq1) < candidates and left <= right:
                heapq.heappush(pq1, costs[left])
                left += 1

            while len(pq2) < candidates and left <= right:
                heapq.heappush(pq2, costs[right])
                right -= 1

            # When element in costs array <= candidates
            if not pq1: 
                heapq.heappush(pq1, float("inf"))
            if not pq2: 
                heapq.heappush(pq2, float("inf"))
            
            # Choose cheapest worker
            if pq1[0] <= pq2[0]:
                total_cost += heapq.heappop(pq1)
            else:
                total_cost += heapq.heappop(pq2)

            k -= 1
        
        return total_cost
    