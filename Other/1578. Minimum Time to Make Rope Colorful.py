# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/description/

class Solution(object):
    def minCost(self, colors, neededTime):
        min_time = 0
        last_max = 0

        for i in range(len(colors)):
            if colors[i] != colors[i-1]:
                last_max = 0
            
            min_time += min(last_max, neededTime[i])    # Add cost of popped balloon
            last_max = max(last_max, neededTime[i])     # Keep track of previous non-popped cost

        return min_time