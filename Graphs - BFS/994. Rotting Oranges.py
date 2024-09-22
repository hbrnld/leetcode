# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan-v2&envId=leetcode-75

from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols= len(grid), len(grid[0])
        
        q = deque()
        fresh_oranges = 0
        
        for i in range(rows):
            for j in range(cols):
                # Append rotten oranges in the queue to start bfs from
                if grid[i][j] == 2:
                    q.append((i,j,0))
                # Count total fresh oranges
                elif grid[i][j] == 1:
                    fresh_oranges += 1
        
        # If no fresh oranges to start with, return 0
        if not fresh_oranges:
            return 0
        
        while q:
            x, y, count = q.popleft()
        
            directions = [[0,1], [0,-1], [1,0], [-1,0]]

            for dx, dy in directions:
                x_new, y_new = x + dx, y + dy

                if (0 <= x_new < rows and 0 <= y_new < cols and grid[x_new][y_new] == 1):
                    q.append((x_new, y_new, count+1))
                    grid[x_new][y_new] = 2
                    fresh_oranges -= 1
                    
        # If we still have fresh oranges left return -1
        if fresh_oranges >= 1:
            return -1
            
        return count