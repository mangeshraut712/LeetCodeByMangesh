from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if not matrix:
            return result

        m = len(matrix)
        n = len(matrix[0])
        top, bottom, left, right = 0, m - 1, 0, n - 1

        while top <= bottom and left <= right:
            # Traverse Right
            for c in range(left, right + 1):
                result.append(matrix[top][c])
            top += 1

            # Traverse Down
            if top <= bottom:
                for r in range(top, bottom + 1):
                    result.append(matrix[r][right])
                right -= 1

            # Traverse Left
            if top <= bottom and left <= right:
                for c in range(right, left - 1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1

            # Traverse Up
            if top <= bottom and left <= right:
                for r in range(bottom, top - 1, -1):
                    result.append(matrix[r][left])
                left += 1

        return result