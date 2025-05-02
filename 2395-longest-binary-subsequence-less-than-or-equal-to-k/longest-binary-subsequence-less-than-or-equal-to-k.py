class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        value = 0       # current numeric value of our subsequence
        length = 0      # current bit‐length of our subsequence

        # Scan from the end (least‐significant bit) toward the front
        for ch in reversed(s):
            if ch == '0':
                # zeros never increase value, always add to length
                length += 1
            else:
                # a 1 would contribute 2^length if we append it
                weight = 1 << length
                if value + weight <= k:
                    value += weight
                    length += 1
                # otherwise skip this '1'

        return length
