from typing import List

class Solution:
    def getWordsInLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        n = len(words)
        if not n:
            return []

        dp = [1] * n
        prev_indices = [-1] * n
        
        for i in range(n):
            len_words_i = len(words[i])
            word_i_val = words[i]

            for j in range(i):
                if groups[j] == groups[i] or len(words[j]) != len_words_i:
                    continue

                hamming_dist = 0
                word_j_val = words[j]
                for k_char_idx in range(len_words_i):
                    if word_j_val[k_char_idx] != word_i_val[k_char_idx]:
                        hamming_dist += 1
                    if hamming_dist > 1: 
                        break 
                
                if hamming_dist == 1:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        prev_indices[i] = j
        
        max_len = 0
        end_idx_of_longest = 0 
        if n > 0:
            max_len = dp[0]
            end_idx_of_longest = 0
            for k_loop_idx in range(1, n): 
                if dp[k_loop_idx] > max_len:
                    max_len = dp[k_loop_idx]
                    end_idx_of_longest = k_loop_idx
            
        result_words = [""] * max_len 
        current_path_ptr = max_len - 1
        current_trace_idx = end_idx_of_longest
        
        while current_trace_idx != -1:
            result_words[current_path_ptr] = words[current_trace_idx]
            current_path_ptr -= 1
            current_trace_idx = prev_indices[current_trace_idx]
        
        return result_words