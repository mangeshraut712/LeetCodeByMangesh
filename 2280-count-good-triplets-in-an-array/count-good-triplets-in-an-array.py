from typing import List

class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        pos2 = [0] * n
        for i in range(n):
            pos2[nums2[i]] = i

        mapped_pos2 = [0] * n
        for i in range(n):
            mapped_pos2[i] = pos2[nums1[i]]

        def update(bit: List[int], index: int, val: int):
            index += 1 # 1-based index for BIT
            while index < len(bit):
                bit[index] += val
                index += index & (-index)

        def query(bit: List[int], index: int) -> int:
            index += 1 # 1-based index for BIT
            res = 0
            while index > 0:
                res += bit[index]
                index -= index & (-index)
            return res

        bit_left = [0] * (n + 1)
        count_left = [0] * n
        for j in range(n):
            p2_y = mapped_pos2[j]
            count_left[j] = query(bit_left, p2_y - 1) # Count elements with pos2 < p2_y
            update(bit_left, p2_y, 1)

        bit_right = [0] * (n + 1)
        count_right = [0] * n
        for j in range(n - 1, -1, -1):
            p2_y = mapped_pos2[j]
            # Count elements with pos2 > p2_y
            # Total elements seen so far to the right = (n - 1 - j)
            # Count elements seen so far with pos2 <= p2_y = query(bit_right, p2_y)
            # Count elements seen so far with pos2 > p2_y = (n - 1 - j) - query(bit_right, p2_y) 
            # Alternative: Query total count (query(bit_right, n-1)) - query(bit_right, p2_y)
            count_right[j] = query(bit_right, n - 1) - query(bit_right, p2_y)
            update(bit_right, p2_y, 1)
            
        total_triplets = 0
        for j in range(n): # Iterate through all possible middle elements
            # Need long long for intermediate product in other languages, Python handles large integers
            if count_left[j] > 0 and count_right[j] > 0:
                 total_triplets += count_left[j] * count_right[j]

        return total_triplets
