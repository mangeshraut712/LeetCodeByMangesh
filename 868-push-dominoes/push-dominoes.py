from typing import List

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Add sentinels to handle edge cases uniformly
        s = 'L' + dominoes + 'R'
        n = len(s)
        # Convert to list for mutability
        res = list(s)

        # 'left' pointer tracks the index of the last encountered 'L' or 'R'
        left = 0

        # 'right' pointer iterates through the string
        for right in range(1, n):
            # If the current domino is '.', continue to the next one
            if s[right] == '.':
                continue

            # If the current domino is 'L' or 'R', we have a segment between 'left' and 'right'
            # that consists only of '.'.
            # The behavior of this segment depends on the states of s[left] and s[right].

            # Case 1: Both ends push in the same direction (L...L or R...R)
            if s[left] == s[right]:
                # Fill the segment between 'left' and 'right' with that direction
                for k in range(left + 1, right):
                    res[k] = s[left]

            # Case 2: Opposing pushes (R...L)
            elif s[left] == 'R' and s[right] == 'L':
                # The dominoes in the middle fall towards their respective pushers
                # They meet in the middle and stop if the segment length is odd,
                # or balance each other if the segment length is even.
                l, r = left + 1, right - 1
                while l < r:
                    res[l] = 'R'
                    res[r] = 'L'
                    l += 1
                    r -= 1

            # Case 3: Opposing pushes (L...R) - The dominoes in between remain standing ('.')
            # This is the default state, so no action is needed for this case.

            # Move the left pointer to the current position for the next segment
            left = right

        # Remove the sentinels from the result before joining and returning
        return ''.join(res[1:-1])
