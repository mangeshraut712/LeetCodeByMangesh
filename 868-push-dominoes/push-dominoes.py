class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        # Pad the string with sentinels so we can handle edges uniformly.
        # We pretend there’s an ‘L’ at index 0 and an ‘R’ at index n+1.
        s = 'L' + dominoes + 'R'
        n = len(s)
        res = list(s)
        
        # i will mark the index of the last seen non-'.' domino
        i = 0  
        # Scan j from 1 to n-1 (the added sentinel at n-1 is 'R')
        for j in range(1, n):
            if s[j] == '.':
                continue
            
            # Now s[i] and s[j] are either 'L' or 'R', and
            # everything between (i,j) is '.' in the original.
            if j - i > 1:
                # Case 1: same direction pushes from both ends
                if s[i] == s[j]:
                    # fill all in-between with that same direction
                    for k in range(i+1, j):
                        res[k] = s[i]
                
                # Case 2: opposing pushes R ... L
                elif s[i] == 'R' and s[j] == 'L':
                    # fill inward from both ends
                    l, r = i+1, j-1
                    while l < r:
                        res[l] = 'R'
                        res[r] = 'L'
                        l += 1
                        r -= 1
                # Case 3: L ... R → they remain standing (“.”), so do nothing
            
            # Move the “last anchor” forward
            i = j
        
        # Drop the sentinels before returning
        return ''.join(res[1:-1])
