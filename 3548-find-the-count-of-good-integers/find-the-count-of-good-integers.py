import math
import collections

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        memo_perm = {}
        def permutations_count(counts):
            key = tuple(sorted((d, f) for d, f in counts.items()))
            if key in memo_perm:
                return memo_perm[key]

            digits_len = sum(counts.values())
            res = math.factorial(digits_len)
            for count in counts.values():
                res //= math.factorial(count)
                
            if 0 in counts and counts[0] > 0:
                counts_copy = counts.copy()
                counts_copy[0] -= 1
                digits_len -= 1
                leading_zero_perms = 0
                if digits_len > 0:
                    leading_zero_perms = math.factorial(digits_len)
                    for count in counts_copy.values():
                        if count > 0:
                            leading_zero_perms //= math.factorial(count)
                res -= leading_zero_perms
                
            memo_perm[key] = res
            return res

        if n == 1:
            count = 0
            for i in range(1, 10):
                if i % k == 0:
                    count += 1
            return count

        half_len = (n + 1) // 2
        start_half = 10**(half_len - 1) if half_len > 1 else 1
        end_half = 10**half_len - 1

        valid_multisets = set()

        for first_half_val in range(start_half, end_half + 1):
            first_half_str = str(first_half_val)
            second_half_str = first_half_str[:-1][::-1] if n % 2 == 1 else first_half_str[::-1]
            palindrome_str = first_half_str + second_half_str
            
            if len(palindrome_str) != n:
                continue

            palindrome_val = int(palindrome_str)
            
            if palindrome_val % k == 0:
                digit_counts = collections.Counter(palindrome_str)
                digit_counts = {int(d): c for d, c in digit_counts.items()}
                multiset_key = tuple(sorted(digit_counts.items()))
                valid_multisets.add(multiset_key)

        total_good_integers = 0

        for multiset_key in valid_multisets:
            counts_dict = dict(multiset_key)
            total_digits = sum(counts_dict.values())
            if total_digits == n:
                num_perms = permutations_count(counts_dict)
                total_good_integers += num_perms

        return total_good_integers