# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        d1, d2 = {}, {}
        output = 0

        for i in range(n):
            row = str(grid[i])
            col = str([grid[j][i] for j in range(n)])

            if row in d1:
                d1[row] += 1
            else:
                d1[row] = 1
            
            if col in d2:
                d2[col] += 1
            else:
                d2[col] = 1

        unique = set(d1.keys()).intersection(d2.keys())

        for key in unique:
            output += (d1.get(key, 0) * d2.get(key, 0))
            
        return output

    def equalPairs2(self, grid):
        from collections import defaultdict
        d = defaultdict(int)
        
        for row in grid:
            d[tuple(row)] += 1
        
        return sum(d[tuple(col)] for col in zip(*grid))   