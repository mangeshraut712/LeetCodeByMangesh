from typing import List
from collections import defaultdict

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        counts = defaultdict(int)
        for a, b in dominoes:
            # Normalize the domino by sorting the pair and converting to a tuple
            normalized_domino = tuple(sorted((a, b)))
            counts[normalized_domino] += 1

        total_pairs = 0
        # If a domino appears n times, the number of pairs is n * (n - 1) // 2
        for count in counts.values():
            if count > 1:
                total_pairs += count * (count - 1) // 2

        return total_pairs
