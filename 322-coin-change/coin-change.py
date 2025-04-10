from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        
        # BFS: queue of (remaining_amount, num_coins)
        queue = deque([(amount, 0)])
        visited = {amount}
        
        while queue:
            remaining, num_coins = queue.popleft()
            
            for coin in coins:
                next_amount = remaining - coin
                if next_amount < 0:
                    continue
                if next_amount == 0:
                    return num_coins + 1
                if next_amount not in visited:
                    visited.add(next_amount)
                    queue.append((next_amount, num_coins + 1))
        
        return -1