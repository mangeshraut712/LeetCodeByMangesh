from typing import List

class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        grid = [[1] * n for _ in range(n)]
        for r, c in mines:
            grid[r][c] = 0

        # dp[r][c] will store the minimum of the lengths of consecutive 1s
        # extending up, down, left, and right from grid[r][c].
        # This minimum value is the order of the largest plus sign centered at (r, c).
        dp = [[0] * n for _ in range(n)]

        # Calculate lengths of consecutive 1s upwards and leftwards
        up = [[0] * n for _ in range(n)]
        left = [[0] * n for _ in range(n)]
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    up[r][c] = (up[r-1][c] + 1) if r > 0 else 1
                    left[r][c] = (left[r][c-1] + 1) if c > 0 else 1

        # Calculate lengths of consecutive 1s downwards and rightwards
        down = [[0] * n for _ in range(n)]
        right = [[0] * n for _ in range(n)]
        for r in range(n - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if grid[r][c] == 1:
                    down[r][c] = (down[r+1][c] + 1) if r < n - 1 else 1
                    right[r][c] = (right[r][c+1] + 1) if c < n - 1 else 1

        max_order = 0
        for r in range(n):
            for c in range(n):
                # The order of the plus sign centered at (r, c) is limited by the shortest arm
                order = min(up[r][c], down[r][c], left[r][c], right[r][c])
                dp[r][c] = order # Store this for clarity, although not strictly needed for the final answer
                max_order = max(max_order, order)

        return max_order