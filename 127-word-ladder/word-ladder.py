import collections
from typing import List
import string

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q_begin = collections.deque([(beginWord, 1)])
        q_end = collections.deque([(endWord, 1)])
        
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        while q_begin and q_end:
            
            # Expand the smaller queue
            if len(q_begin) <= len(q_end):
                level_len = len(q_begin)
                queue = q_begin
                visited_curr = visited_begin
                visited_other = visited_end
            else:
                level_len = len(q_end)
                queue = q_end
                visited_curr = visited_end
                visited_other = visited_begin

            for _ in range(level_len):
                word, length = queue.popleft()

                if word in visited_other:
                    return length + visited_other[word] - 1

                for i in range(len(word)):
                    original_char = word[i]
                    for char_code in range(ord('a'), ord('z') + 1):
                        char = chr(char_code)
                        if char == original_char:
                            continue
                        
                        next_word = word[:i] + char + word[i+1:]
                        
                        if next_word in word_set and next_word not in visited_curr:
                            visited_curr[next_word] = length + 1
                            queue.append((next_word, length + 1))
                    
        return 0
