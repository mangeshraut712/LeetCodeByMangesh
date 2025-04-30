from typing import List
from collections import deque

class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        max_val = max(nums)

        prime_score = [0] * (max_val + 1)
        for p in range(2, max_val + 1):
            if prime_score[p] == 0:
                for i in range(p, max_val + 1, p):
                    prime_score[i] += 1

        nums_prime_scores = [prime_score[x] for x in nums]

        left_boundary = [-1] * n
        stack = deque()
        for i in range(n):
            while stack and nums_prime_scores[stack[-1]] < nums_prime_scores[i]:
                stack.pop()
            if stack:
                left_boundary[i] = stack[-1]
            stack.append(i)

        right_boundary = [n] * n
        stack = deque()
        for i in range(n - 1, -1, -1):
            while stack and nums_prime_scores[stack[-1]] <= nums_prime_scores[i]:
                stack.pop()
            if stack:
                right_boundary[i] = stack[-1]
            stack.append(i)

        opportunities = []
        for i in range(n):
            count = (i - left_boundary[i]) * (right_boundary[i] - i)
            opportunities.append((nums[i], count))

        opportunities.sort(key=lambda x: x[0], reverse=True)

        total_score = 1

        def power(base, exp):
            res = 1
            base %= MOD
            while exp > 0:
                if exp % 2 == 1:
                    res = (res * base) % MOD
                base = (base * base) % MOD
                exp //= 2
            return res

        for value, count in opportunities:
            ops_to_take = min(k, count)
            total_score = (total_score * power(value, ops_to_take)) % MOD
            k -= ops_to_take
            if k == 0:
                break

        return total_score
