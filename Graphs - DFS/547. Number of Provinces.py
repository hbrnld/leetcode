# https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        seen = set()
        provinces = 0

        if not isConnected:
            return 0

        def dfs(current):
            for city, link in enumerate(isConnected[current]):
                if (link == 1) and (city not in seen):
                    seen.add(city)
                    dfs(city)
        
        for city in range(len(isConnected)):
            if city not in seen:
                dfs(city)
                provinces += 1

        return provinces