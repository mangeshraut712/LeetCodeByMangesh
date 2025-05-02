from typing import List
from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        result = list(dominoes)

        forces_from_R = [float('inf')] * n
        current_force_R = float('inf')
        for i in range(n):
            if dominoes[i] == 'R':
                current_force_R = 0
            elif dominoes[i] == 'L':
                current_force_R = float('inf')
            elif current_force_R != float('inf'):
                current_force_R += 1
            forces_from_R[i] = current_force_R

        forces_from_L = [float('inf')] * n
        current_force_L = float('inf')
        for i in range(n - 1, -1, -1):
            if dominoes[i] == 'L':
                current_force_L = 0
            elif dominoes[i] == 'R':
                current_force_L = float('inf')
            elif current_force_L != float('inf'):
                current_force_L += 1
            forces_from_L[i] = current_force_L

        for i in range(n):
            if dominoes[i] == '.':
                if forces_from_R[i] < forces_from_L[i]:
                    result[i] = 'R'
                elif forces_from_L[i] < forces_from_R[i]:
                    result[i] = 'L'

        return "".join(result)
