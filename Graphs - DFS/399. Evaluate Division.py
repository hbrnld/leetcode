# https://leetcode.com/problems/evaluate-division/description/?envType=study-plan-v2&envId=leetcode-75

from collections import defaultdict

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        graph = defaultdict(dict)

        for (u, v), val in zip(equations, values):
            graph[u][u] = graph[v][v] = 1
            graph[u][v] = val
            graph[v][u] = 1 / val

        for k in graph:
            for i in graph[k]:
                for j in graph[k]:
                    graph[i][j] = graph[i][k] * graph[k][j]

        return [graph[u].get(v, -1) for u, v in queries]