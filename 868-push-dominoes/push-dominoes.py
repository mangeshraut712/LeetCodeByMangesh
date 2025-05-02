from typing import List
from collections import deque

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        state = [(-1, None) for _ in range(n)]
        q = deque()

        for i in range(n):
            if dominoes[i] == 'L':
                state[i] = (0, 'L')
                q.append(i)
            elif dominoes[i] == 'R':
                state[i] = (0, 'R')
                q.append(i)

        while q:
            current_idx = q.popleft()
            current_time, current_direction = state[current_idx]

            if current_direction == 'R':
                next_idx = current_idx + 1
                if next_idx < n:
                    next_time, next_direction = state[next_idx]
                    if next_time == -1:
                        state[next_idx] = (current_time + 1, 'R')
                        q.append(next_idx)
                    elif next_time == current_time + 1:
                        if next_direction == 'L':
                            state[next_idx] = (current_time + 1, '.')

            elif current_direction == 'L':
                next_idx = current_idx - 1
                if next_idx >= 0:
                    next_time, next_direction = state[next_idx]
                    if next_time == -1:
                        state[next_idx] = (current_time + 1, 'L')
                        q.append(next_idx)
                    elif next_time == current_time + 1:
                        if next_direction == 'R':
                            state[next_idx] = (current_time + 1, '.')

        final_dominoes = []
        for _, direction in state:
            if direction is None or direction == '.':
                final_dominoes.append('.')
            else:
                final_dominoes.append(direction)

        return "".join(final_dominoes)
