from typing import List

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []
        prev = None
        for w, g in zip(words, groups):
            if prev is None or g != prev:
                res.append(w)
                prev = g
        return res
