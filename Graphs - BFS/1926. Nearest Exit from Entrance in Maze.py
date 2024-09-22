# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """

        rows = len(maze)
        cols = len(maze[0])
        directions = [(-1,0), (1,0), (0,1), (0,-1)]

        queue = deque([(entrance[0],entrance[1],0)])
        maze[entrance[0]][entrance[1]]="+"
        
        while queue:
            x, y, steps = queue.popleft()

            for i, j in directions:
                x_new, y_new = x+i, y+j

                # Empty cell within bounds
                if 0 <= x_new < rows and 0 <= y_new < cols and maze[x_new][y_new] == ".": 

                    # If we reach the boundary
                    if x_new == 0 or x_new == rows-1 or y_new == 0 or y_new == cols - 1:
                        return steps + 1
                    
                    maze[x_new][y_new]="+"
                    queue.append((x_new, y_new, steps+1))

        return -1
        