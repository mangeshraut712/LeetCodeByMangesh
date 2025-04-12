import math
import collections
from typing import List # Optional import

class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        
        memo_perm = {}
        def permutations_count(counts):
            key = tuple(sorted(counts.items()))
            if key in memo_perm:
                return memo_perm[key]

            digits_len = sum(counts.values())
            res = math.factorial(digits_len)
            for count in counts.values():
                res //= math.factorial(count)
                
            if 0 in counts and counts[0] > 0:
                counts[0] -= 1
                digits_len -= 1
                if digits_len >= 0: # Check if length became negative (only possible if counts[0] was the only item initially)
                    leading_zero_perms = math.factorial(digits_len)
                    for count in counts.values():
                         if count > 0: # Factorial of negative is invalid
                             leading_zero_perms //= math.factorial(count)
                         elif count < 0: # Should not happen if logic is correct
                             leading_zero_perms = 0 
                             break 
                    res -= leading_zero_perms
                # Restore counts[0] for subsequent calls if counts is reused (it's not here)
                # counts[0] += 1 # Not needed as counts is local copy from Counter
                
            memo_perm[key] = res
            return res

        valid_multisets = set()
        
        half_len = (n + 1) // 2
        start_half = 10**(half_len - 1) if half_len > 0 else 0 # Adjust for n=0? No, n>=1
        end_half = 10**half_len - 1

        # Special handling for n=1
        if n == 1:
             count = 0
             for i in range(1, 10):
                 if i % k == 0:
                     count += 1
             return count

        for first_half_val in range(start_half, end_half + 1):
            first_half_str = str(first_half_val)
            
            second_half_str = ""
            if n % 2 == 1:
                second_half_str = first_half_str[:-1][::-1]
            else:
                second_half_str = first_half_str[::-1]
                
            palindrome_str = first_half_str + second_half_str
            
            # Ensure correct length (handles cases like n=2, half_len=1, start=1)
            if len(palindrome_str) != n: continue
            # Ensure no leading zero (handled by start_half range)
            # if palindrome_str[0] == '0': continue 

            palindrome_val = int(palindrome_str)
            
            if palindrome_val % k == 0:
                digit_counts = collections.Counter(palindrome_str)
                # Convert Counter to a hashable type (tuple of sorted items) for the set
                multiset_key = tuple(sorted(digit_counts.items()))
                valid_multisets.add(multiset_key)

        total_good_integers = 0
        processed_multisets_for_perm_calc = set()

        for multiset_key in valid_multisets:
             # Convert back to dictionary/Counter for permutation calculation
             counts_dict = dict(multiset_key)
             # Need to convert digit char back to int for counts_dict keys if needed by perm func
             # Assuming perm func takes counts keyed by int digits 0-9
             
             # Recalculate counts properly as Counter expects hashable items (chars ok)
             temp_counts = collections.Counter()
             total_digits = 0
             for digit_char, count in counts_dict.items():
                 temp_counts[int(digit_char)] = count
                 total_digits += count

             # Ensure the multiset represents exactly n digits
             if total_digits == n:
                 # Calculate permutations for this multiset
                 num_perms = permutations_count(temp_counts)
                 total_good_integers += num_perms

        return total_good_integers