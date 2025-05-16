class Solution:
    def getWordsInLongestSubsequence(self, words: list[str], groups: list[int]) -> list[str]:
        # PASTE STARTING FROM HERE, INDENTED CORRECTLY
        n = len(words)
        if not n:
            return []

        dp = [1] * n
        prev_indices = [-1] * n

        for i in range(n):
            for j in range(i):
                if groups[j] != groups[i] and len(words[j]) == len(words[i]):
                    hamming_dist = 0
                    for char_idx in range(len(words[j])):
                        if words[j][char_idx] != words[i][char_idx]:
                            hamming_dist += 1
                    
                    if hamming_dist == 1:
                        if dp[j] + 1 > dp[i]:
                            dp[i] = dp[j] + 1
                            prev_indices[i] = j
        
        max_length = 0
        current_end_idx = 0 
        if n > 0:
            for i in range(n):
                if dp[i] > max_length:
                    max_length = dp[i]
                    current_end_idx = i
        
        result_words = []
        idx_iterator = current_end_idx
        while idx_iterator != -1:
            result_words.append(words[idx_iterator])
            idx_iterator = prev_indices[idx_iterator]
        
        return result_words[::-1]
        # END OF PASTED BODY