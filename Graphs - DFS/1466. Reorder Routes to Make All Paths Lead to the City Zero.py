# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/description/?envType=study-plan-v2&envId=leetcode-75

from collections import defaultdict, deque

class Solution(object):
    def minReorder(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        
        graph = defaultdict(list)
        for src, dest in connections:
            graph[src].append((dest, 1))
            graph[dest].append((src, 0))
        
        q = deque([0])
        visited = set([0])
        swaps = 0
        
        while q:
            curr = q.popleft()
            for child, cost in graph[curr]:
                if child not in visited:
                    visited.add(child)
                    swaps += cost
                    q.append(child)
                    
        return swaps