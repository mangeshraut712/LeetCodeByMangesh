class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)

        def hamming(a, b):
            return sum(x != y for x, y in zip(a, b))

        dp = [1] * n
        prev = [-1] * n

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and len(words[j]) == len(words[i]) and hamming(words[j], words[i]) == 1:
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
