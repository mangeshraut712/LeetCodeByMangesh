from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        if len(strs) == 1:
            return strs[0]
            
        first_str = strs[0]
        if not first_str:
             return ""

        for i in range(len(first_str)):
            char_to_match = first_str[i]
            for j in range(1, len(strs)):
                current_str = strs[j]
                if i >= len(current_str) or current_str[i] != char_to_match:
                    return first_str[:i]
                    
        return first_str
