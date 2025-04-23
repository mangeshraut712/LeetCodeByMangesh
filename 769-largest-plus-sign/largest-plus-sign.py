from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0

        left = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        up = [[0] * n for _ in range(n)]
        down = [[0] * n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    left[i][j] = (left[i][j - 1] if j > 0 else 0) + 1
                    up[i][j] = (up[i - 1][j] if i > 0 else 0) + 1

        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if grid[i][j]:
                    right[i][j] = (right[i][j + 1] if j < n - 1 else 0) + 1
                    down[i][j] = (down[i + 1][j] if i < n - 1 else 0) + 1

        max_order = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    order = min(up[i][j], down[i][j], left[i][j], right[i][j])
                    max_order = max(max_order, order)

        return max_order
