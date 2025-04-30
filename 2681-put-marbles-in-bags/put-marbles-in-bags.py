from typing import List

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)

        # If k is 1, there's only one bag containing all marbles.
        # The cost is weights[0] + weights[n-1].
        # The minimum and maximum scores are the same, so the difference is 0.
        if k == 1:
            return 0

        # The problem can be rephrased as choosing k-1 cut points.
        # Each cut point between index i and i+1 adds weights[i] + weights[i+1] to the total score.
        # To minimize the score difference, we want to choose the k-1 smallest adjacent sums for the minimum score
        # and the k-1 largest adjacent sums for the maximum score.
        adjacent_sums = []
        for i in range(n - 1):
            adjacent_sums.append(weights[i] + weights[i+1])

        # Sort the adjacent sums to easily pick the smallest and largest
        adjacent_sums.sort()

        # Sum the k-1 smallest adjacent sums for the minimum score
        min_sum_cuts = sum(adjacent_sums[:k-1])

        # Sum the k-1 largest adjacent sums for the maximum score
        # Using negative indexing gets the last k-1 elements
        max_sum_cuts = sum(adjacent_sums[-(k-1):])

        # The difference between the maximum and minimum scores is the difference
        # between the sum of the k-1 largest adjacent sums and the sum of the k-1 smallest adjacent sums.
        return max_sum_cuts - min_sum_cuts
