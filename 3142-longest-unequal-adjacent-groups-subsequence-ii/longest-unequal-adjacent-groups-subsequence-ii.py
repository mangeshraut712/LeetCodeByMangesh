class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        # Bucket indices by length
        length_map = {}
        for i, w in enumerate(words):
            l = len(w)
            if l not in length_map:
                length_map[l] = []
            length_map[l].append(i)

        def hamming(a, b):
            return sum(x != y for x, y in zip(a, b))

        dp = [1] * n
        prev = [-1] * n

        for l, indices in length_map.items():
            for i in indices:
                for j in indices:
                    if j >= i: continue  # only check j < i
                    if groups[j] != groups[i] and hamming(words[j], words[i]) == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev[i] = j

        max_len = max(dp)
        idx = dp.index(max_len)
        seq = []
        while idx != -1:
            seq.append(words[idx])
            idx = prev[idx]
        return seq[::-1]
