from collections import Counter
from typing import List

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        answer_counts = Counter(answers)
        minimum_rabbits = 0

        for answer, count in answer_counts.items():
            num_groups = (count + answer) // (answer + 1)
            minimum_rabbits += num_groups * (answer + 1)

        return minimum_rabbits