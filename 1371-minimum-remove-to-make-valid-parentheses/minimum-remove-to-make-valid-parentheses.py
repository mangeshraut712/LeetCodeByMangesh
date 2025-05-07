from typing import List

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # mark removals directly on a single list
        a = list(s)
        st = []
        ap, pp = st.append, st.pop
        for i, c in enumerate(a):
            if c == '(':
                ap(i)
            elif c == ')':
                if st:
                    pp()
                else:
                    a[i] = ''      # mark unmatched ')'
        # remove any unmatched '('
        for i in st:
            a[i] = ''
        return ''.join(a)
