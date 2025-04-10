import collections
from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q_begin = collections.deque([(beginWord, 1)])  # Length = number of words in path so far
        q_end = collections.deque([(endWord, 1)])
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}

        alphabet = 'abcdefghijklmnopqrstuvwxyz'

        while q_begin and q_end:
            # Expand the smaller queue
            if len(q_begin) <= len(q_end):
                queue, visited_curr, visited_other = q_begin, visited_begin, visited_end
            else:
                queue, visited_curr, visited_other = q_end, visited_end, visited_begin

            for _ in range(len(queue)):
                word, length = queue.popleft()

                # Check for intersection
                if word in visited_other:
                    return length + visited_other[word] - 1  # Total words = steps from both sides - 1 (overlap)

                # Generate next words
                for i in range(len(word)):
                    for char in alphabet:
                        if char == word[i]:
                            continue
                        next_word = word[:i] + char + word[i+1:]
                        if next_word in word_set and next_word not in visited_curr:
                            queue.append((next_word, length + 1))
                            visited_curr[next_word] = length + 1
        
        return 0