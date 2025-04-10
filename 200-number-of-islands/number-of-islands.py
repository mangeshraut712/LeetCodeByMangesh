from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    queue = deque([(r, c)])
                    grid[r][c] = '0'  # Mark as visited
                    
                    # BFS to explore the island
                    while queue:
                        row, col = queue.popleft()
                        for dr, dc in directions:
                            new_r, new_c = row + dr, col + dc
                            if 0 <= new_r < rows and 0 <= new_c < cols and grid[new_r][new_c] == '1':
                                queue.append((new_r, new_c))
                                grid[new_r][new_c] = '0'
        
        return island_count